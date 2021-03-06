import json
import argparse
import trie
import pickle
import os


def search(search_term):
    # people_list = tr.search(search_term)

    if search_term not in word_map:
        print("Word {} was not found. Try another one!".format(search_term))
    else:
        people_list = word_map[search_term]
        for p in people_list:
            with open('people_small/' + p) as f:
                data = json.load(f)
                if search_term in data:
                    print("emails by {} containing '{}': {}".format(p, search_term, data[search_term]))


    get_completions(search_term)

def get_completions(search_term):
    tr.getChildren(search_term)


if __name__ == '__main__':
    print("Initializing....")
    # open the mapping from words to individuals
    with open('word_map_small.json') as f:
        word_map = json.load(f)

    # Open the word trie file created by process.py
    trie_data = os.environ.get('WORD_TRIE','word_trie_small.pkl')
    file_object = open(trie_data,'rb')

    # load the object from the file into "tr"
    tr = pickle.load(file_object)
    print("loaded trie: ", tr)
    print("Please enter a word to search for. Hit 'Enter' with no search term to exit")
    search_term = input("search term: ")
    search(search_term)

    # Initialize prompt for user
    while True:
        search_term = input("search term: ")
        if len(search_term) == 0:
            break
        else:
            search(search_term)
