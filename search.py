import json
import argparse
import trie
import pickle


def search(search_term):
    people_list = tr.search(search_term)
    if not people_list:
        print("Word {} was not found. Try another one!".format(search_term))
    else:
        for p in people_list[1]:
            with open('people/' + p) as f:
                data = json.load(f)
                print("emails by {} containing '{}': {}".format(p, search_term, data[search_term]))

    if tr.prefixExists(search_term):
        getCompletions(search_term)
        
def getCompletions(search_term):
    # hasPrefix = tr.prefixExists(search_term)
    # if hasPrefix:
    tr.getChildren(search_term)

if __name__ == '__main__':
    # Open the trie file created by process.py
    print("Initializing....")
    file_object = open('email_trie','rb')

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
