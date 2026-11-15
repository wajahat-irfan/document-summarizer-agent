#!/usr/bin/env python3
"""
document-summarizer-agent -- extractive text summarizer, no API key needed.

Method: word-frequency extractive summarization.
  1. Split the text into sentences.
  2. Count word frequencies, ignoring common stopwords.
  3. Score each sentence by the sum of its words' frequencies.
  4. Return the top N sentences, in their original order.

Usage:
    python summarizer.py sample_document.txt
    python summarizer.py sample_document.txt --sentences 5
    python summarizer.py myfile.txt --sentences 2
"""

import argparse
import re
import sys
from collections import Counter

STOPWORDS = set("""
a an the and or but if then else for of to in on at by with without from as is are was were
be been being have has had do does did will would shall should can could may might must
i you he she it we they me him her us them my your his its our their this that these those
there here what when where who whom which why how all any both each few more most other
some such no nor not only own same so than too very just also because until while about
into through after over between out against during before again once here there when where
""".split())


def split_sentences(text):
    """Split text into sentences on . ! ? followed by whitespace."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p.strip() for p in parts if p.strip()]


def tokenize(sentence):
    """Lowercase word tokens (letters only)."""
    return re.findall(r"[a-z]+", sentence.lower())


def summarize(text, n_sentences=3):
    """Return the top n_sentences, in original order."""
    sentences = split_sentences(text)
    if not sentences:
        return []
    if n_sentences >= len(sentences):
        return sentences

    words = [w for s in sentences for w in tokenize(s) if w not in STOPWORDS]
    freq = Counter(words)

    scored = []
    for i, sentence in enumerate(sentences):
        tokens = [w for w in tokenize(sentence) if w not in STOPWORDS]
        # Average frequency keeps long sentences from always winning.
        score = sum(freq[w] for w in tokens) / max(len(tokens), 1)
        scored.append((score, i, sentence))

    top = sorted(scored, key=lambda x: x[0], reverse=True)[:n_sentences]
    top.sort(key=lambda x: x[1])  # back to original order
    return [s for _, _, s in top]


def main():
    parser = argparse.ArgumentParser(description="Extractive text summarizer (no API key).")
    parser.add_argument("file", help="Text file to summarize.")
    parser.add_argument("--sentences", type=int, default=3, help="Number of sentences (default: 3).")
    args = parser.parse_args()

    if args.sentences < 1:
        print("Error: --sentences must be at least 1.", file=sys.stderr)
        return 1

    try:
        with open(args.file, encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Error: file not found: {args.file}", file=sys.stderr)
        return 1

    sentences = split_sentences(text)
    summary = summarize(text, args.sentences)

    print(f"File: {args.file} ({len(sentences)} sentences)")
    print(f"Summary ({len(summary)} sentences):")
    print()
    for s in summary:
        print("- " + s)
    return 0


if __name__ == "__main__":
    sys.exit(main())
