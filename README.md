# Enron Search

A trie-based implementation of a mini search engine for Enron emails

## Usage
Clone this repository. Run `python search.py`

After initialization, try searching for a term in the emails.

Example:
```
$ python search.py
Initializing....

Please enter a word to search for. Hit 'Enter' with no search term to exit
search term: hi
emails by arnold-j containing 'hi': ['287.', '363.', '868.']
emails by lavorato-j containing 'hi': ['86.', '419.']
emails by symes-k containing 'hi': ['1368.', '3117.', '1388.', '1108.', '1365.', '1067.', '3041.', '2550.', '1387.', '2528.', '2760.', '1360.', '3115.']
emails by wolfe-j containing 'hi': ['36.', '117.']
emails by mcconnell-m containing 'hi': ['1013.', '1025.']

search term: bye
Word bye was not found. Try another one!
```


### process.py
From the Enron email dataset, creates the following mappings:  
`word -> individuals with this word in their mailbox`  
The words in this map are used to create a trie and "autocomplete" functionality

`word -> email id's containing word (for each individual)`

### search.py
Queries the trie for the search term, returning a list of individuals whose inboxes contain that term. Then, get the exact email id's for each individual
