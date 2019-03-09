# Enron Search

A trie-based implementation of a mini search engine for Enron emails

## process.py
From the Enron email dataset, creates a mapping of word to senders (and email id's). Loads the words and emails into a trie for searching through emails by words and prefixes.

## search.py
Usage: `python search.py <word>`
Queries the trie for the search term, returning a list of senders and emails that contain that term
