import json
import argparse

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

    parser = argparse.ArgumentParser()
    parser.add_argument('word',
                    help='a word to search in emails')
    args = parser.parse_args()
    search_term = args.word

    trie = Trie()

    # CREATES THE TRIE 
    # TODO: this should be done only once, offline
    with open('mail_map.json') as f:
        data = json.load(f)
        for word in data:
            trie.insert(word, data[word])

    print("search result: ", trie.search(search_term))
