from ArqProject import *
from structsArq import *
from Trie_mainBin import *
import pickle
import os
import csv
import re


def Trie_mkfile_Title(listdatas):
    trie_title = Trie()

    f = open(r"src\bin\title_trie.bin", "wb")

    for line in listdatas:
        title = line.title
        id_title = line.id_title
        trie_title.insert(title, id_title)

    pickle.dump(trie_title, f, pickle.HIGHEST_PROTOCOL)
    f.close()


def Trie_mkfile_Netflix(listdatas):
    trie_netflix = TrieNetflix()

    f = open(r"src\bin\netflix_trie.bin", "wb")

    for line in listdatas:
        id_title = line.id_title
        id_languages = line.id_languages
        id_styear = line.id_styear
        id_type = line.id_type
        id_country = line.id_country
        id_rankpop = line.id_rankpop
        trie_netflix.insert(id_title, id_languages, id_styear,
                            id_type, id_country, id_rankpop)

    pickle.dump(trie_netflix, f, pickle.HIGHEST_PROTOCOL)
    f.close()


def Trie_mkfile_Language(listdatas):
    trie_language = Trie()

    f = open(r"src\bin\language_trie.bin", "wb")

    for line in listdatas:
        language = line.language
        id_language = line.id_language
        trie_language.insert(language, id_language)

    pickle.dump(trie_language, f, pickle.HIGHEST_PROTOCOL)
    f.close()


def Trie_mkfile_StartYear(listdatas):
    trie_styear = Trie()

    f = open(r"src\bin\styear_styear.bin", "wb")

    for line in listdatas:
        styear = line.styear
        id_styear = line.id_styear
        trie_styear.insert(str(styear), id_styear)

    pickle.dump(trie_styear, f, pickle.HIGHEST_PROTOCOL)
    f.close()


def Trie_mkfile_Type(listdatas):
    trie_type = Trie()

    f = open(r"src\bin\type_trie.bin", "wb")

    for line in listdatas:
        type = line.type
        id_type = line.id_type
        trie_type.insert(type, id_type)

    pickle.dump(trie_type, f, pickle.HIGHEST_PROTOCOL)
    f.close()


def Trie_mkfile_Country(listdatas):
    trie_country = Trie()

    f = open(r"src\bin\country_trie.bin", "wb")

    for line in listdatas:
        country = line.country
        id_country = line.id_country
        trie_country.insert(country, id_country)

    pickle.dump(trie_country, f, pickle.HIGHEST_PROTOCOL)
    f.close()


def Trie_mkfile_RankPop(listdatas):
    trie_rankpop = Trie()

    f = open(r"src\bin\rankpop_trie.bin", "wb")

    for line in listdatas:
        rankpop = line.rankpop
        id_rankpop = line.id_rankpop
        trie_rankpop.insert(str(rankpop), id_rankpop)

    pickle.dump(trie_rankpop, f, pickle.HIGHEST_PROTOCOL)
    f.close()


def CsvtoBin():
    f = open(r"src\csv\NetflixVideosDataCPD.csv",
             'r', errors='ignore', encoding="UTF-8")
    NetflixVideosData = []
    nd = 0
    if os.path.isfile(r"src\bin\NetflixVideosDataCPD.bin") == False:
        with open(r"src\bin\NetflixVideosDataCPD.bin", "wb") as handler_bin:
            arquivo_csv = csv.reader(f, dialect='excel', delimiter=",")
            for t, line in enumerate(arquivo_csv):
                if t == 0:
                    del line
                else:
                    i = 5
                    for x in line[5::1]:
                        i += 1
                    xbin = NetflixVideos(nd, line)
                    NetflixVideosData.append(xbin)
                    pickle.dump(xbin, handler_bin, pickle.HIGHEST_PROTOCOL)
                    nd += 1
        handler_bin.close()
    f.close()

    f = open(r"src\csv\TitleDataCPD.csv", 'r',
             errors='ignore', encoding="UTF-8")
    TitleDataCPD = []
    nd1 = 0
    if os.path.isfile(r"src\bin\TitleDataCPD.bin") == False:
        with open(r"src\bin\TitleDataCPD.bin", "wb") as handler_bin1:
            arquivo_csv = csv.reader(f, dialect='excel', delimiter=",")
            for t, line in enumerate(arquivo_csv):
                if t == 0:
                    del line
                else:
                    i = 1
                    for x in line[1::1]:
                        i += 1
                    xbin = TitleCPD(nd1, line)
                    TitleDataCPD.append(xbin)
                    pickle.dump(xbin, handler_bin1, pickle.HIGHEST_PROTOCOL)
                    nd1 += 1
        handler_bin1.close()
    f.close()

    f = open(r"src\csv\LanguageDataCPD.csv", 'r',
             errors='ignore', encoding="UTF-8")
    LanguageDataCPD = []
    nd2 = 0
    if os.path.isfile(r"src\bin\LanguageDataCPD.bin") == False:
        with open(r"src\bin\LanguageDataCPD.bin", "wb") as handler_bin:
            arquivo_csv = csv.reader(f, dialect='excel', delimiter=",")
            for t, line in enumerate(arquivo_csv):
                if t == 0:
                    del line
                else:
                    i = 1
                    for x in line[1::1]:
                        i += 1
                    xbin = LanguageCPD(nd2, line)
                    LanguageDataCPD.append(xbin)
                    pickle.dump(xbin, handler_bin, pickle.HIGHEST_PROTOCOL)
                    nd2 += 1
        handler_bin.close()
    f.close()

    f = open(r"src\csv\StartYearDataCPD.csv", 'r',
             errors='ignore', encoding="UTF-8")
    StartYearDataCPD = []
    nd3 = 0
    if os.path.isfile(r"src\bin\StartYearDataCPD.bin") == False:
        with open(r"src\bin\StartYearDataCPD.bin", "wb") as handler_bin:
            arquivo_csv = csv.reader(f, dialect='excel', delimiter=",")
            for t, line in enumerate(arquivo_csv):
                if t == 0:
                    del line
                else:
                    i = 1
                    for x in line[1::1]:
                        i += 1
                    xbin = StartYearCPD(nd3, line)
                    StartYearDataCPD.append(xbin)
                    pickle.dump(xbin, handler_bin, pickle.HIGHEST_PROTOCOL)
                    nd3 += 1
        handler_bin.close()
    f.close()

    f = open(r"src\csv\TypeDataCPD.csv", 'r',
             errors='ignore', encoding="UTF-8")
    TypeDataCPD = []
    nd4 = 0
    if os.path.isfile(r"src\bin\TypeDataCPD.bin") == False:
        with open(r"src\bin\TypeDataCPD.bin", "wb") as handler_bin:
            arquivo_csv = csv.reader(f, dialect='excel', delimiter=",")
            for t, line in enumerate(arquivo_csv):
                if t == 0:
                    del line
                else:
                    i = 1
                    for x in line[1::1]:
                        i += 1
                    xbin = TypeCPD(nd4, line)
                    TypeDataCPD.append(xbin)
                    pickle.dump(xbin, handler_bin, pickle.HIGHEST_PROTOCOL)
                    nd4 += 1
        handler_bin.close()
    f.close()

    f = open(r"src\csv\CountryOriginDataCPD.csv",
             'r', errors='ignore', encoding="UTF-8")
    CountryOriginDataCPD = []
    nd5 = 0
    if os.path.isfile(r"src\bin\CountryOriginDataCPD.bin") == False:
        with open(r"src\bin\CountryOriginDataCPD.bin", "wb") as handler_bin:
            arquivo_csv = csv.reader(f, dialect='excel', delimiter=",")
            for t, line in enumerate(arquivo_csv):
                if t == 0:
                    del line
                else:
                    i = 1
                    for x in line[1::1]:
                        i += 1
                    xbin = CountryOriginCPD(nd5, line)
                    CountryOriginDataCPD.append(xbin)
                    pickle.dump(xbin, handler_bin, pickle.HIGHEST_PROTOCOL)
                    nd5 += 1
        handler_bin.close()
    f.close()

    f = open(r"src\csv\PopularRankDataCPD.csv",
             'r', errors='ignore', encoding="UTF-8")
    PopularRankDataCPD = []
    nd6 = 0
    if os.path.isfile(r"src\bin\PopularRankDataCPD.bin") == False:
        with open(r"src\bin\PopularRankDataCPD.bin", "wb") as handler_bin:
            arquivo_csv = csv.reader(f, dialect='excel', delimiter=",")
            for t, line in enumerate(arquivo_csv):
                if t == 0:
                    del line
                else:
                    i = 1
                    for x in line[1::1]:
                        i += 1
                    xbin = PopularRankCPD(nd6, line)
                    PopularRankDataCPD.append(xbin)
                    pickle.dump(xbin, handler_bin, pickle.HIGHEST_PROTOCOL)
                    nd6 += 1
        handler_bin.close()
    f.close()

    Trie_mkfile_Title(TitleDataCPD)
    Trie_mkfile_Netflix(NetflixVideosData)
    Trie_mkfile_Language(LanguageDataCPD)
    Trie_mkfile_StartYear(StartYearDataCPD)
    Trie_mkfile_Type(TypeDataCPD)
    Trie_mkfile_Country(CountryOriginDataCPD)
    Trie_mkfile_RankPop(PopularRankDataCPD)
