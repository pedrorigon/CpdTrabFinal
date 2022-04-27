from CsvConverterBinary import *
from ArqProject import *
from structsArq import *
from Trie_mainBin import *
from operator import delitem
import hashlib
import pandas as pd
import numpy as np
import pickle
import os
import csv
import re

#CsvtoBin()

#trie2 = TrieNetflix()
#trie2.insert(str(20), 21, 24, 2, 3, 3222)

#print(trie2.id_rankpopSearch("20"))

#print(trie.idSearch("daniel"))
#print(trie.starts_with('e'))  insert(self, id_title, id_languages, id_styear, id_type, id_country, id_rankpop):



#trie_netflix = TrieNetflix()

word = 'mai'


modelo = open(r"src\bin\title_trie.bin", "rb")
tree = pickle.load(modelo)
modelo.close()
n = tree.starts_with(word)

print(n)
