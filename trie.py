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
