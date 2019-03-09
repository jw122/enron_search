import json
import argparse
import trie
import pickle

if __name__ == '__main__':
    # Open the trie file created by process.py
    print("Initializing....")
    fileObject = open('email_trie','rb')

    # load the object from the file into "tr"
    tr = pickle.load(fileObject)
    print("loaded trie: ", tr)
    print("Please enter a word to search for. Hit 'Enter' with no search term to exit")

    # Initialize prompt for user
    while True:
        search_term = input("search term: ")
        if len(search_term) == 0:
            break
        else:
            res = tr.search(search_term)
            if not res:
                print("Word {} was not found. Try another one!".format(search_term))
            else:
                print("Word found in the following people's emails: ", res[1])


    # the term " " can be found in the following emails
