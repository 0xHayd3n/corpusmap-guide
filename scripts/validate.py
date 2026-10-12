#!/usr/bin/env python3
"""Validate this reading companion, not the paper's experimental results.

Uses the Python standard library. Checks UTF-8 text, local Markdown paths and
GitHub-style heading anchors, v1 paper locators, citation/metadata consistency,
selective result arithmetic, and excluded source/private materials.
"""

from __future__ import annotations

import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
VERSION = "2609.37226v1"
TITLE = "Follow the Entities: A Corpus Map for Agentic Search"
AUTHORS = ["Soyeong Jeong", "Sujay Kumar Jauhar", "Sung Ju Hwang", "Andrew Joohun Nam"]
ERRORS: list[str] = []


def require(condition: bool, message: str) -> None:
    if not condition:
        ERRORS.append(message)


def headings(text: str) -> set[str]:
    """Produce anchors for the simple ATX headings used in this repository."""
    anchors: set[str] = set()
    seen: dict[str, int] = {}
    in_fence = False
    for line in text.splitlines():
        if line.startswith("```"):
            in_fence = not in_fence
        if in_fence:
            continue
        match = re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", line)
        if not match:
            continue
        title = match.group(1).lower().replace("`", "")
        title = re.sub(r"[^\w\- ]", "", title, flags=re.UNICODE).replace(" ", "-")
        count = seen.get(title, 0)
        seen[title] = count + 1
        anchors.add(title if count == 0 else f"{title}-{count}")
    return anchors


def main() -> int:
    files = [p for p in ROOT.rglob("*") if p.is_file() and ".git" not in p.relative_to(ROOT).parts]
    texts: dict[Path, str] = {}
    for path in files:
        relative = path.relative_to(ROOT).as_posix()
        require(path.suffix.lower() not in {".pdf", ".png", ".jpg", ".jpeg", ".webp"}, f"Excluded source/image: {relative}")
        require(not any(part in {"source-local", "private-transfer", ".env", ".venv"} for part in path.relative_to(ROOT).parts), f"Private/intermediate path: {relative}")
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeError:
            ERRORS.append(f"Not UTF-8 text: {relative}")
            continue
        texts[path] = text
        require(text.endswith("\n"), f"Missing final newline: {relative}")
        require(not any(ord(c) < 32 and c not in "\n\r\t" for c in text), f"Control character: {relative}")
        require("\ufffd" not in text, f"Replacement character: {relative}")
        if path.suffix != ".py":
            require(not re.search(r"libfile_|oaiusercontent|download_url|sig=", text), f"Private transfer identifier/data: {relative}")
        if path.suffix == ".md":
            require(len(re.findall(r"^```", text, re.M)) % 2 == 0, f"Unbalanced code fence: {relative}")
            require(len(re.findall(r"^\$\$\s*$", text, re.M)) % 2 == 0, f"Unbalanced math fence: {relative}")

    link_count = 0
    for path, text in texts.items():
        if path.suffix != ".md" and path.name != "llms.txt":
            continue
        for match in re.finditer(r"\[[^\]\n]+\]\(([^\s)]+)(?:\s+[^)]*)?\)", text):
            link_count += 1
            target = unquote(match.group(1).strip("<>"))
            parsed = urlparse(target)
            if parsed.scheme:
                if parsed.netloc == "arxiv.org" and parsed.path.startswith(("/abs/2609.37226", "/pdf/2609.37226", "/html/2609.37226")):
                    require(VERSION in parsed.path, f"Unpinned paper link: {path.name}: {target}")
                    if parsed.fragment:
                        require(bool(re.fullmatch(r"page=(?:[1-9]|1[0-9]|2[0-9])", parsed.fragment)), f"Invalid PDF page locator: {target}")
                continue
            destination = (path.parent / parsed.path).resolve() if parsed.path else path
            require(destination.is_relative_to(ROOT), f"Link escapes repository: {path.name}: {target}")
            require(destination.is_file(), f"Missing local link: {path.name}: {target}")
            if parsed.fragment and destination in texts:
                require(parsed.fragment in headings(texts[destination]), f"Missing anchor: {path.name}: {target}")

    try:
        metadata = json.loads((ROOT / "metadata.json").read_text(encoding="utf-8"))
        results = json.loads((ROOT / "data/main-comparison.json").read_text(encoding="utf-8"))
        paper = metadata["paper"]
        require(paper["title"] == TITLE, "Paper title mismatch")
        require([a["name"] for a in paper["authors"]] == AUTHORS, "Paper author order mismatch")
        require(paper["versioned_id"] == VERSION and paper["pages"] == 29, "Source version/page mismatch")
        require(paper["submitted_at"] == "2026-09-29T10:39:57Z", "Submission date mismatch")
        require(paper["doi"] == "10.48550/arXiv.2609.37226", "DOI mismatch")
        require(metadata["repository"]["owner"] == "0xHayd3n", "Repository owner mismatch")
        require(not metadata["repository"]["curator_is_paper_author"], "Curator misattributed")
        require(not metadata["companion"]["official"] and not metadata["companion"]["experiments_reproduced"], "Unsupported official/reproduction status")
        require(paper["official_code_url"] is None and paper["official_project_url"] is None, "Unverified official link")
        require(not metadata["provenance"]["attachment_byte_equality_verified"], "Unsupported byte-equality claim")
        for role, target in metadata["navigation"].items():
            require((ROOT / target).is_file(), f"Missing navigation target {role}: {target}")
        require(results["source_version"] == VERSION, "Results version mismatch")
        require(len(results["comparisons"]) == 4, "Main model count mismatch")
        for row in results["comparisons"]:
            delta = row["corpusmap_overall_quality"] - row["raw_overall_quality"]
            require(abs(delta - row["reported_quality_gain_points"]) <= 0.02, f"Gain/rounding inconsistency: {row['model']}")
            reduction = 100 * (1 - row["relative_input_tokens"])
            require(abs(reduction - row["approximate_aggregate_token_reduction_percent"]) < 0.001, f"Token reduction error: {row['model']}")
            low, high = row["reported_gain_ci95_points"]
            require(0 < low < row["reported_quality_gain_points"] < high, f"Invalid gain interval: {row['model']}")
            require(f"{row['raw_overall_quality']:.2f}" in texts[ROOT / "README.md"] and f"{row['corpusmap_overall_quality']:.2f}" in texts[ROOT / "README.md"], f"README score inconsistency: {row['model']}")
    except (KeyError, ValueError, OSError) as exc:
        ERRORS.append(f"Structured metadata failure: {exc}")

    cff = texts.get(ROOT / "CITATION.cff", "")
    bib = texts.get(ROOT / "references/paper.bib", "")
    require("cff-version: 1.2.0" in cff and "preferred-citation:" in cff, "Missing CFF citation structure")
    require(TITLE in cff and TITLE in bib and VERSION in cff and VERSION in bib, "Citation title/version inconsistency")
    for author in AUTHORS:
        given, family = author.rsplit(" ", 1)
        require(f"family-names: {family}" in cff and f"given-names: {given}" in cff, f"Missing preferred-citation author: {author}")
        require(f"{family}, {given}" in bib, f"Missing BibTeX author: {author}")
    require(bib.count("{") == bib.count("}"), "Unbalanced BibTeX braces")

    if ERRORS:
        print("Content validation FAILED:")
        for error in ERRORS:
            print(f"- {error}")
        return 1
    print(f"Content validation passed: {len(files)} UTF-8 files, {link_count} Markdown links, local anchors, pinned locators, metadata/citations, and result arithmetic.")
    print("This is documentation validation. No paper experiment was run.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
