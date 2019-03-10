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

    def prefixExists(self, prefix):
        currNode = self.root
        for char in prefix:
            if char not in currNode.children:
                return False
            # print("found char: ", char)
            # print("children: ", currNode.children)
            currNode = currNode.children[char]
        return True

    def getChildren(self, prefix):
        currNode = self.root
        for char in prefix:
            if char in currNode.children:
                currNode = currNode.children[char]
        # find options for remaining characters
        completions = []
        self.getOptions(prefix, currNode, completions)
        print("------------")
        print("completions for this term: ", completions)

    def getOptions(self, prefix, node, options):

        if not node.children:
            options.append(prefix)

        for c in node.children:
            candidate = prefix + c
            self.getOptions(candidate, node.children[c], options)
