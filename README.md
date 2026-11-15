# Document Summarizer Agent

**Author:** Wajahat Irfan, BS Computer Science student (7th semester), GPGC No. 1 Abbottabad

## What it does
Summarizes a text file without any API key. It uses **word-frequency
extractive summarization**: it counts how often each meaningful word appears
(ignoring common stopwords), scores every sentence by the frequency of its
words, and returns the top N sentences in their original order.

## How to run
```bash
cd document-summarizer-agent
python summarizer.py sample_document.txt
python summarizer.py sample_document.txt --sentences 5
python summarizer.py myfile.txt --sentences 2
```

## Example output
```
File: sample_document.txt (15 sentences)
Summary (3 sentences):

- Artificial intelligence is changing the way small businesses work every day.
- Many shop owners now use simple AI tools to answer customer questions automatically.
- When used carefully, AI automation helps small businesses grow without hiring extra staff.
```

## Skills shown
- Python, `argparse`, `re` (regular expressions), `collections.Counter`
- Text processing: tokenization, stopword removal, sentence splitting
- Extractive summarization algorithm (word-frequency scoring)
