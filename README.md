# Enron Search

A trie-based implementation of a mini search engine for Enron emails

## process.py
From the Enron email dataset, creates a mapping of word to individuals, and word to emails (for each individual). Loads the words and emails into a trie for searching through emails by words and prefixes.

## search.py
Usage: `python search.py`
Queries the trie for the search term, returning a list of senders and emails that contain that term

Example:
```
$ python search.py
Initializing....

Please enter a word to search for. Hit 'Enter' with no search term to exit

search term: hi
Word found in the following people's emails:  ['arnold-j', 'lavorato-j', 'symes-k', 'wolfe-j', 'mcconnell-m']
```
