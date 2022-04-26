from ArqProject import *
from CsvConverterBinary import *
import re
import pickle

class TrieNode:
    def __init__(self, value):
        self.index = 0
        self.value = value         
        self.children = {}
        self.isEndOfWord = False

    def __str__(self):
        return self.value

class Trie:
    def __init__(self):
        self.root = TrieNode("_")
        
    def insert(self, word, index):
        current = self.root

        for letter in word:
            if letter not in current.children:
                current.children[letter] = TrieNode(letter)
            current = current.children[letter]
        current.isEndOfWord = True
        current.index = index

    def search(self, word):
        pointer = self.root
        for letter in word:
            if letter not in pointer.children:
                return False
            pointer = pointer.children[letter]
        return pointer.isEndOfWord

    def starts_with(self, prefix):
        words = []
        starting_node = self.get_node(prefix)
        self.Group(starting_node, prefix, words)

        return words

    def Group(self, root, prefix, words):
        if root is None:
            return None
        if root != self.root:
            if root.isEndOfWord:
                words.append(prefix)
        for value, node in root.children.items():
            self.Group(node, prefix + value, words)

    def get_node(self, prefix):
        pointer = self.root
        for letter in prefix:
            if letter not in pointer.children:
                return None
            pointer = pointer.children[letter]
        return pointer
    
    def idSearch(self, word):
        pointer = self.root
        for letter in word:
            if letter not in pointer.children:
                return False
            pointer = pointer.children[letter]
        return pointer.index











