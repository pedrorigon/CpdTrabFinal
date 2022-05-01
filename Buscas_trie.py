from CsvConverterBinary import *
from ArqProject import *
from structsArq import *
from Trie_mainBin import *
#import pickle

def Busca_id_titleporid_language(id_language):
    modelo = open(r"src\bin\CabecalhoPrincipal.bin", "rb")
    inf = pickle.load(modelo)
    modelo.close()
    lenArq = inf.nd
    list_id_title = []
    modelo = open(r"src\bin\NetflixVideosDataCPD.bin", "rb")
    for i in range(lenArq):
        line = pickle.load(modelo)
        if line.id_languages == id_language:
            list_id_title.append(line.id_title)
    modelo.close()
    return list_id_title

def id_title_eh_movie(id_title):
    modelo = open(r"src\bin\CabecalhoPrincipal.bin", "rb")
    inf = pickle.load(modelo)
    modelo.close()
    lenArq = inf.nd
    modelo = open(r"src\bin\NetflixVideosDataCPD.bin", "rb")
    for i in range(lenArq):
        line = pickle.load(modelo)
        if line.id_title == id_title:
            if line.id_type == "2":
                modelo.close()
                return True    
            else:
                modelo.close()
                return False
    modelo.close()
    return False

def id_title_eh_movie_e_pais(id_title, id_country):
    modelo = open(r"src\bin\CabecalhoPrincipal.bin", "rb")
    inf = pickle.load(modelo)
    modelo.close()
    lenArq = inf.nd
    id_country = str(id_country)
    modelo = open(r"src\bin\NetflixVideosDataCPD.bin", "rb")
    for i in range(lenArq):
        line = pickle.load(modelo)
        if line.id_title == id_title:
            if line.id_type == "2":
                if line.id_country == id_country:
                    modelo.close()
                    return True
    modelo.close()
    return False

def Busca_id_titleporid_styear(id_styear):
    modelo = open(r"src\bin\CabecalhoPrincipal.bin", "rb")
    inf = pickle.load(modelo)
    modelo.close()
    lenArq = inf.nd
    list_id_title = []
    modelo = open(r"src\bin\NetflixVideosDataCPD.bin", "rb")
    for i in range(lenArq):
        line = pickle.load(modelo)
        if line.id_styear == id_styear:
            list_id_title.append(line.id_title)
    modelo.close()
    return list_id_title

def Busca_id_titleporid_type(id_type):
    modelo = open(r"src\bin\CabecalhoPrincipal.bin", "rb")
    inf = pickle.load(modelo)
    modelo.close()
    lenArq = inf.nd
    list_id_title = []
    modelo = open(r"src\bin\NetflixVideosDataCPD.bin", "rb")
    for i in range(lenArq):
        line = pickle.load(modelo)
        if line.id_type == id_type:
            list_id_title.append(line.id_title)
    modelo.close()
    return list_id_title

def Busca_id_titleporid_country(id_country):
    modelo = open(r"src\bin\CabecalhoPrincipal.bin", "rb")
    inf = pickle.load(modelo)
    modelo.close()
    lenArq = inf.nd
    list_id_title = []
    modelo = open(r"src\bin\NetflixVideosDataCPD.bin", "rb")
    for i in range(lenArq):
        line = pickle.load(modelo)
        if line.id_country == id_country:
            list_id_title.append(line.id_title)
    modelo.close()
    return list_id_title

def Busca_id_titleporid_rankpop(id_rankpop):
    entryflag = 0
    modelo = open(r"src\bin\CabecalhoPrincipal.bin", "rb")
    inf = pickle.load(modelo)
    modelo.close()
    lenArq = inf.nd
    list_id_title = []
    modelo = open(r"src\bin\NetflixVideosDataCPD.bin", "rb")
    for i in range(lenArq):
        line = pickle.load(modelo)
        if line.id_rankpop == id_rankpop:
            entryflag = 1
            list_id_title.append(line.id_title)
    modelo.close()
    if entryflag == 1:
        return list_id_title
    else:
        list_erro = False
        return list_erro

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

def Busca_id_languages(language):

    f = open(r"src\bin\language_trie.bin", "rb")
    tree = pickle.load(f)
    f.close()
    n = tree.idSearch(language)
    
    return n

def Busca_styear(id_styear):
    f = open(r"src\bin\styear_styearinvertido.bin", "rb")
    tree = pickle.load(f)
    f.close()
    n = tree.idSearch(id_styear)
    return n

def Busca_id_styear(styear):

    f = open(r"src\bin\styear_styear.bin", "rb")
    tree = pickle.load(f)
    f.close()
    n = tree.idSearch(styear)

    return n

def Busca_type(id_type):

    f = open(r"src\bin\type_trieinvertido.bin", "rb")
    tree = pickle.load(f)
    f.close()
    n = tree.idSearch(id_type)

    return n

def Busca_id_type(type):

    f = open(r"src\bin\type_trie.bin", "rb")
    tree = pickle.load(f)
    f.close()
    n = tree.idSearch(type)

    return n

def Busca_country(id_country):

    f = open(r"src\bin\country_trieinvertido.bin", "rb")
    tree = pickle.load(f)
    f.close()
    n = tree.idSearch(id_country)

    return n


def Busca_id_country(country):

    f = open(r"src\bin\country_trie.bin", "rb")
    tree = pickle.load(f)
    f.close()
    n = tree.idSearch(country)

    return n

def Busca_rankpop(id_rankpop):

    f = open(r"src\bin\rankpop_trieinvertido.bin", "rb")
    tree = pickle.load(f)
    f.close()
    n = tree.idSearch(id_rankpop)

    return n

def Busca_id_rankpop(rankpop):

    f = open(r"src\bin\rankpop_trie.bin", "rb")
    tree = pickle.load(f)
    f.close()
    n = tree.idSearch(rankpop)

    return n

def Busca_id_type_por_id_title(id_title):
    f = open(r"src\bin\netflix_trie.bin", "rb")
    tree = pickle.load(f)
    f.close()
    n = tree.id_typeSearch(id_title)

    return n

def Busca_id_country_por_id_title(id_title):
    f = open(r"src\bin\netflix_trie.bin", "rb")
    tree = pickle.load(f)
    f.close()
    n = tree.id_countrySearch(id_title)

    return n

def Busca_id_languages_por_id_title(id_title):
    f = open(r"src\bin\netflix_trie.bin", "rb")
    tree = pickle.load(f)
    f.close()
    n = tree.id_languagesSearch(id_title)

    return n

def Busca_id_styear_por_id_title(id_title):
    f = open(r"src\bin\netflix_trie.bin", "rb")
    tree = pickle.load(f)
    f.close()
    n = tree.id_styearSearch(id_title)

    return n

def Busca_id_rankpop_por_id_title(id_title):
    f = open(r"src\bin\netflix_trie.bin", "rb")
    tree = pickle.load(f)
    f.close()
    n = tree.id_rankpopSearch(id_title)

    return n
