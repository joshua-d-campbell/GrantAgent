#!/usr/bin/env python3
"""Readability check for an NIH Project Narrative (public health relevance statement).

Zero-dependency: standard library only, so it runs in any environment.
Scores Flesch-Kincaid Grade Level and Flesch Reading Ease, counts sentences
and per-sentence word lengths, and reports pass/fail against the narrative
targets. Exit code 0 = all checks pass, 1 = at least one fails.

Usage:
    python3 check_readability.py narrative.txt
    python3 check_readability.py --text "Paste the narrative here."
    echo "Paste the narrative here." | python3 check_readability.py

Optional flags:
    --max-sentences N   (default 3)
    --max-grade X       (default 9.0; target band is 7-8)
    --min-ease X        (default 60.0)
    --max-sentence-words N  (default 25)

Syllable counting uses a heuristic (vowel groups with silent-e handling),
the same approach most readability tools use. Scores can differ from other
tools by a few tenths of a point; treat the numbers as a guide, not an oracle.
"""

import argparse
import re
import sys

VOWELS = "aeiouy"

# Common abbreviations that end with a period but do not end a sentence.
ABBREVIATIONS = {
    "dr", "mr", "mrs", "ms", "prof", "st", "vs", "etc", "e.g", "i.e",
    "u.s", "fig", "no", "al",
}


def split_sentences(text: str) -> list:
    """Split text into sentences on ., !, ? — with light abbreviation handling."""
    text = " ".join(text.split())  # normalize whitespace
    # Protect decimal numbers (e.g., 2.5) from splitting
    protected = re.sub(r"(\d)\.(\d)", r"\1<DOT>\2", text)
    parts = re.split(r"(?<=[.!?])\s+", protected)
    sentences, buffer = [], ""
    for part in parts:
        candidate = (buffer + " " + part).strip() if buffer else part
        last_word = re.findall(r"[\w.]+(?=[.!?]$)", candidate)
        if last_word and last_word[-1].rstrip(".").lower() in ABBREVIATIONS:
            buffer = candidate  # abbreviation, keep accumulating
        else:
            sentences.append(candidate)
            buffer = ""
    if buffer:
        sentences.append(buffer)
    return [s.replace("<DOT>", ".") for s in sentences if re.search(r"\w", s)]


def words_in(sentence: str) -> list:
    return re.findall(r"[A-Za-z0-9'’-]+", sentence)


def count_syllables(word: str) -> int:
    """Heuristic syllable count: vowel groups, minus silent trailing 'e'."""
    w = re.sub(r"[^a-z]", "", word.lower())
    if not w:
        return 0
    groups = re.findall(rf"[{VOWELS}]+", w)
    count = len(groups)
    # Silent final e ("nose", "pipeline") — but not "le" after a consonant ("simple")
    if w.endswith("e") and not w.endswith("le") and count > 1:
        count -= 1
    return max(count, 1)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("file", nargs="?", help="text file containing the narrative")
    parser.add_argument("--text", help="narrative text passed inline")
    parser.add_argument("--max-sentences", type=int, default=3)
    parser.add_argument("--max-grade", type=float, default=9.0)
    parser.add_argument("--min-ease", type=float, default=60.0)
    parser.add_argument("--max-sentence-words", type=int, default=25)
    args = parser.parse_args()

    if args.text is not None:
        text = args.text
    elif args.file:
        with open(args.file, encoding="utf-8") as fh:
            text = fh.read()
    elif not sys.stdin.isatty():
        text = sys.stdin.read()
    else:
        parser.error("provide a file, --text, or piped stdin")

    sentences = split_sentences(text)
    if not sentences:
        print("No sentences found.")
        return 1

    all_words = [w for s in sentences for w in words_in(s)]
    n_sent, n_words = len(sentences), len(all_words)
    n_syll = sum(count_syllables(w) for w in all_words)

    wps = n_words / n_sent
    spw = n_syll / n_words
    grade = 0.39 * wps + 11.8 * spw - 15.59
    ease = 206.835 - 1.015 * wps - 84.6 * spw

    print(f"Sentences: {n_sent}   Words: {n_words}   Syllables: {n_syll}")
    print(f"Words/sentence: {wps:.1f}   Syllables/word: {spw:.2f}")
    print(f"Flesch-Kincaid Grade Level: {grade:.1f}   (target ~7-8, max {args.max_grade:g})")
    print(f"Flesch Reading Ease:        {ease:.1f}   (target 60-70, min {args.min_ease:g})")
    print()

    checks = [
        (f"Sentence count <= {args.max_sentences}", n_sent <= args.max_sentences),
        (f"Grade level <= {args.max_grade:g}", grade <= args.max_grade),
        (f"Reading ease >= {args.min_ease:g}", ease >= args.min_ease),
    ]
    long_sentences = [(i + 1, len(words_in(s)), s) for i, s in enumerate(sentences)
                      if len(words_in(s)) > args.max_sentence_words]
    checks.append((f"Every sentence <= {args.max_sentence_words} words", not long_sentences))

    ok = True
    for label, passed in checks:
        print(f"  [{'PASS' if passed else 'FAIL'}] {label}")
        ok = ok and passed

    # Revision targets: what to fix first if anything failed
    if not ok:
        print("\nRevision targets:")
        if n_sent > args.max_sentences:
            print(f"  - Over the sentence cap ({n_sent} > {args.max_sentences}): merge related ideas or cut"
                  " a sentence, then swap in shorter words to hold the grade level down.")
        for idx, n, s in long_sentences:
            print(f"  - Sentence {idx} has {n} words: \"{s[:70]}...\"" if len(s) > 70
                  else f"  - Sentence {idx} has {n} words: \"{s}\"")
        hard_words = sorted(
            {w.lower() for w in all_words if count_syllables(w) >= 4},
            key=lambda w: -count_syllables(w))
        if hard_words:
            print(f"  - Long words (4+ syllables) to swap for shorter ones: {', '.join(hard_words[:10])}")
        if grade > args.max_grade and n_sent < args.max_sentences:
            print("  - A sentence can still be split (grade level responds most to sentence length).")
        elif grade > args.max_grade:
            print("  - Already at the sentence cap: shorten words and cut clauses instead of splitting.")

    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
