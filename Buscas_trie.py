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

def Busca_title(id_title):

    modelo = open(r"src\bin\title_trieinvertido.bin", "rb")
    tree = pickle.load(modelo)
    modelo.close()
    n = tree.idSearch(id_title)
    
    return n

def Busca_id_title(word):
    modelo = open(r"src\bin\title_trie.bin", "rb")
    tree = pickle.load(modelo)
    modelo.close()
    n = tree.idSearch(word)
    return n

def Busca_languages(id_languages):

    f = open(r"src\bin\language_trieinvertido.bin", "rb")
    tree = pickle.load(f)
    f.close()
    n = tree.idSearch(id_languages)

    return n

def Busca_id_languages(id_title):

    f = open(r"src\bin\netflix_trie.bin", "rb")
    tree = pickle.load(f)
    f.close()
    n = tree.id_languagesSearch(id_title)
    print(n)
    
    return n

def Busca_styear(id_styear):
    f = open(r"src\bin\styear_styearinvertido.bin", "rb")
    tree = pickle.load(f)
    f.close()
    n = tree.idSearch(id_styear)
    return n

def Busca_id_styear(id_title):

    f = open(r"src\bin\netflix_trie.bin", "rb")
    tree = pickle.load(f)
    f.close()
    n = tree.id_styearSearch(id_title)

    return n

def Busca_type(id_type):

    f = open(r"src\bin\type_trieinvertido.bin", "rb")
    tree = pickle.load(f)
    f.close()
    n = tree.idSearch(id_type)

    return n

def Busca_id_type(id_title):

    f = open(r"src\bin\netflix_trie.bin", "rb")
    tree = pickle.load(f)
    f.close()
    n = tree.id_typeSearch(id_title)

    return n

def Busca_country(id_country):

    f = open(r"src\bin\country_trieinvertido.bin", "rb")
    tree = pickle.load(f)
    f.close()
    n = tree.idSearch(id_country)

    return n


def Busca_id_country(id_title):

    f = open(r"src\bin\netflix_trie.bin", "rb")
    tree = pickle.load(f)
    f.close()
    n = tree.id_countrySearch(id_title)

    return n

def Busca_rankpop(id_rankpop):

    f = open(r"src\bin\rankpop_trieinvertido.bin", "rb")
    tree = pickle.load(f)
    f.close()
    n = tree.idSearch(id_rankpop)

    return n

def Busca_id_rankpop(id_title):

    f = open(r"src\bin\netflix_trie.bin", "rb")
    tree = pickle.load(f)
    f.close()
    n = tree.id_rankpopSearch(id_title)

    return n