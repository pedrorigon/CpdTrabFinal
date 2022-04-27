from CsvConverterBinary import *
from ArqProject import *
from structsArq import *
from Trie_mainBin import *
#import pickle


def Busca_filmePrefix(word):

    modelo = open(r"src\bin\title_trie.bin", "rb")
    tree = pickle.load(modelo)
    modelo.close()
    n = tree.starts_with(word)
    return n


def Busca_id_title(word):
    modelo = open(r"src\bin\title_trie.bin", "rb")
    tree = pickle.load(modelo)
    modelo.close()
    n = tree.idSearch(word)
    return n
