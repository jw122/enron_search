import json
import argparse

'''
A trie with nodes referencing the emails containing them
'''
class Node:
    def __init__(self):
        self.children = {}
        self.wordExists = False
        self.emails = {}

class Trie(object):

    def __init__(self):
        self.root = Node()

    def insert(self, word, emails):
        currNode = self.root
        for char in word:
            if char not in currNode.children:
                currNode.children[char] = Node()
            currNode = currNode.children[char]
        currNode.wordExists = True
        currNode.emails = emails

    def search(self, word):
        currNode = self.root
        for char in word:
            if char not in currNode.children:
                return False
            currNode = currNode.children[char]
        return currNode.wordExists, currNode.emails


    def startsWith(self, prefix):
        currNode = self.root
        for char in prefix:
            if char not in currNode.children:
                return False
            currNode = currNode.children[char]
        return True


if __name__ == '__main__':
    # parse search term
    parser = argparse.ArgumentParser()
    parser.add_argument('word',
                    help='a word to search in emails')
    args = parser.parse_args()
    search_term = args.word

    # CREATES THE TRIE
    # TODO: this should be done only once, offline
    trie = Trie()

    with open('mail_map_small.json') as f:
        data = json.load(f)
        for word in data:
            trie.insert(word, data[word])

    # Actual execution of search query
    print("search result: ", trie.search(search_term))
