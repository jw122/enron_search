# Enron Search

A trie-based implementation of a mini search engine for Enron emails

## Usage
Clone this repository. Run `python search_local.py`

After initialization, try searching for a term in the emails.

Example:
```
$ python search.py
Initializing....

search term: life
emails by arnold-j containing 'life': ['1029.', '248.', '1005.', '1399.', '606.', '732.', '605.', '162.', '354.', '379.', '406.', '361.', '408.', '136.', '609.']
emails by lavorato-j containing 'life': ['112.', '430.', '289.', '277.']
emails by townsend-j containing 'life': ['81.']
emails by symes-k containing 'life': ['1994.', '1722.', '50.', '2803.', '3293.', '1721.', '1483.', '1886.', '84.', '2688.', '2851.', '2779.', '2438.', '2209.', '1127.', '156.', '3124.', '2777.', '69.', '2495.', '959.', '63.', '2510.', '1212.', '895.', '984.', '2327.', '2806.', '2727.', '1586.', '2641.', '2796.', '2775.', '1202.', '1284.', '2854.', '2817.', '1267.', '2757.', '1122.', '2778.', '2439.', '2528.', '1263.', '1493.', '3039.', '2689.', '1398.', '2801.', '2959.', '337.', '2802.', '2217.']
emails by wolfe-j containing 'life': ['109.', '190.', '56.']
emails by mcconnell-m containing 'life': ['838.', '474.', '601.', '642.', '854.', '920.', '574.', '599.', '1013.', '935.', '783.', '1135.', '562.', '122.', '853.', '378.', '668.', '851.', '837.', '1134.', '1025.', '793.', '247.', '843.', '489.', '844.', '847.', '1068.', '856.', '600.']
------------
completions for this term:  ['lifeblood', 'lifesaver', 'lifestyle', 'lifesized', 'lifeas', 'lifelong', 'lifeless', 'lifetime']

search term: bye
Word bye was not found. Try another one!
```

Files ending with `local.py` are intended for local testing and use a smaller subset of the email data.

### process_local.py
From the Enron email dataset, creates the following mappings:  
`word -> individuals with this word in their mailbox`  
The words in this map are used to create a trie for "autocomplete" functionality

`word -> email id's containing word` (for each individual, saved in people/ directory)

### search_local.py
Uses trie to generate completions. Queries the word-to-people mapping, returning a list of individuals whose inboxes contain that term. Then, fetch the exact email id's containing that term in each individual's inbox
