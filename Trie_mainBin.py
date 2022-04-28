from ArqProject import *
from CsvConverterBinary import *
import re
import pickle

class TrieNodeNetflix:
    def __init__(self, word):
        self.id_title= word
        self.id_languages = 0
        self.id_styear = 0
        self.id_type = 0
        self.id_country = 0
        self.id_rankpop = 0
        #self.value = value         
        self.children = {}
        self.isEndOfWord = False

    def __str__(self):
        return self.id_title

class TrieNetflix:
    def __init__(self):
        self.root = TrieNodeNetflix("_")
        
    def insert(self, word, id_languages, id_styear, id_type, id_country, id_rankpop):
        current = self.root

        for letter in word:
            if letter not in current.children:
                current.children[letter] = TrieNodeNetflix(letter)
            current = current.children[letter]
        current.isEndOfWord = True
        current.id_languages = id_languages
        current.id_styear = id_styear
        current.id_type = id_type
        current.id_country = id_country
        current.id_rankpop = id_rankpop

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
    
    def id_languagesSearch(self, word):
        pointer = self.root
        for letter in word:
            if letter not in pointer.children:
                return False
            pointer = pointer.children[letter]
        return pointer.id_languages

    def id_styearSearch(self, word):
        pointer = self.root
        for letter in word:
            if letter not in pointer.children:
                return False
            pointer = pointer.children[letter]
        return pointer.id_styear

    def id_typeSearch(self, word):
        pointer = self.root
        for letter in word:
            if letter not in pointer.children:
                return False
            pointer = pointer.children[letter]
        return pointer.id_type

    def id_countrySearch(self, word):
        pointer = self.root
        for letter in word:
            if letter not in pointer.children:
                return False
            pointer = pointer.children[letter]
        return pointer.id_country

    def id_rankpopSearch(self, word):
        pointer = self.root
        for letter in word:
            if letter not in pointer.children:
                return False
            pointer = pointer.children[letter]
        return pointer.id_rankpop



