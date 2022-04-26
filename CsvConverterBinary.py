from ArqProject import *
from structsArq import *
import pickle
import os
import csv
import re

def Default_str(word):
    aux_word = word.lower()  

    word_list = re.sub("[\W]", " ", aux_word).split()

    return word_list

def Trie_mkfile_Title(listdatas):
    trie_title = Trie()

    f = open(r"src\bin\title_trie.bin", "wb")

    for line in listdatas:
        title = line.title
        id_title = line.id_title
        title_default = Default_str(title)       
        trie_title.insert(title_default, id_title)

    pickle.dump(trie_title, f, pickle.HIGHEST_PROTOCOL)
    f.close()

def CsvtoBin():

    f = open(r"src\csv\NetflixVideosDataCPD.csv", 'r', errors='ignore', encoding="UTF-8")
    NetflixVideosData = []
    nd = 0
    if os.path.isfile(r"src\bin\NetflixVideosDataCPD.bin") == False:
        with open(r"src\bin\NetflixVideosDataCPD.bin", "wb") as handler_bin:
            arquivo_csv = csv.reader(f, dialect='excel', delimiter=",")
            for t, line in enumerate(arquivo_csv):
                if t == 0:
                    del line
                else:
                    i=5
                    for x in line[5::1]:
                        i+=1
                    xbin = NetflixVideos(nd, line)
                    NetflixVideosData.append(xbin)
                    pickle.dump(xbin, handler_bin, pickle.HIGHEST_PROTOCOL)
                    nd += 1               
        handler_bin.close()
    f.close()

    f = open(r"src\csv\TitleDataCPD.csv", 'r', errors='ignore', encoding="UTF-8")
    TitleDataCPD = []
    nd1 = 0
    if os.path.isfile(r"src\bin\TitleDataCPD.bin") == False:
        with open(r"src\bin\TitleDataCPD.bin", "wb") as handler_bin1:
            arquivo_csv = csv.reader(f, dialect='excel', delimiter=",")
            for t, line in enumerate(arquivo_csv):
                if t == 0:
                    del line
                else:
                    i=1
                    for x in line[1::1]:
                        i+=1
                    xbin = TitleCPD(nd1, line)
                    TitleDataCPD.append(xbin)
                    pickle.dump(xbin, handler_bin1, pickle.HIGHEST_PROTOCOL)
                    nd1 += 1               
        handler_bin1.close()
    f.close()

    f = open(r"src\csv\LanguageDataCPD.csv", 'r', errors='ignore', encoding="UTF-8")
    LanguageDataCPD = []
    nd2 = 0
    if os.path.isfile(r"src\bin\LanguageDataCPD.bin") == False:
        with open(r"src\bin\LanguageDataCPD.bin", "wb") as handler_bin:
            arquivo_csv = csv.reader(f, dialect='excel', delimiter=",")
            for t, line in enumerate(arquivo_csv):
                if t == 0:
                    del line
                else:
                    i=1
                    for x in line[1::1]:
                        i+=1
                    xbin = LanguageCPD(nd2, line)
                    LanguageDataCPD.append(xbin)
                    pickle.dump(xbin, handler_bin, pickle.HIGHEST_PROTOCOL)
                    nd2 += 1               
        handler_bin.close()
    f.close()

    f = open(r"src\csv\StartYearDataCPD.csv", 'r', errors='ignore', encoding="UTF-8")
    StartYearDataCPD = []
    nd3 = 0
    if os.path.isfile(r"src\bin\StartYearDataCPD.bin") == False:
        with open(r"src\bin\StartYearDataCPD.bin", "wb") as handler_bin:
            arquivo_csv = csv.reader(f, dialect='excel', delimiter=",")
            for t, line in enumerate(arquivo_csv):
                if t == 0:
                    del line
                else:
                    i=1
                    for x in line[1::1]:
                        i+=1
                    xbin = StartYearCPD(nd3, line)
                    StartYearDataCPD.append(xbin)
                    pickle.dump(xbin, handler_bin, pickle.HIGHEST_PROTOCOL)
                    nd3 += 1               
        handler_bin.close()
    f.close()

    f = open(r"src\csv\TypeDataCPD.csv", 'r', errors='ignore', encoding="UTF-8")
    TypeDataCPD = []
    nd4 = 0
    if os.path.isfile(r"src\bin\TypeDataCPD.bin") == False:
        with open(r"src\bin\TypeDataCPD.bin", "wb") as handler_bin:
            arquivo_csv = csv.reader(f, dialect='excel', delimiter=",")
            for t, line in enumerate(arquivo_csv):
                if t == 0:
                    del line
                else:
                    i=1
                    for x in line[1::1]:
                        i+=1
                    xbin = TypeCPD(nd4, line)
                    TypeDataCPD.append(xbin)
                    pickle.dump(xbin, handler_bin, pickle.HIGHEST_PROTOCOL)
                    nd4 += 1               
        handler_bin.close()
    f.close()

    f = open(r"src\csv\CountryOriginDataCPD.csv", 'r', errors='ignore', encoding="UTF-8")
    CountryOriginDataCPD = []
    nd5 = 0
    if os.path.isfile(r"src\bin\CountryOriginDataCPD.bin") == False:
        with open(r"src\bin\CountryOriginDataCPD.bin", "wb") as handler_bin:
            arquivo_csv = csv.reader(f, dialect='excel', delimiter=",")
            for t, line in enumerate(arquivo_csv):
                if t == 0:
                    del line
                else:
                    i=1
                    for x in line[1::1]:
                        i+=1
                    xbin = CountryOriginCPD(nd5, line)
                    CountryOriginDataCPD.append(xbin)
                    pickle.dump(xbin, handler_bin, pickle.HIGHEST_PROTOCOL)
                    nd5 += 1               
        handler_bin.close()
    f.close()

    f = open(r"src\csv\PopularRankDataCPD.csv", 'r', errors='ignore', encoding="UTF-8")
    PopularRankDataCPD = []
    nd6 = 0
    if os.path.isfile(r"src\bin\PopularRankDataCPD.bin") == False:
        with open(r"src\bin\PopularRankDataCPD.bin", "wb") as handler_bin:
            arquivo_csv = csv.reader(f, dialect='excel', delimiter=",")
            for t, line in enumerate(arquivo_csv):
                if t == 0:
                    del line
                else:
                    i=1
                    for x in line[1::1]:
                        i+=1
                    xbin = PopularRankCPD(nd6, line)
                    PopularRankDataCPD.append(xbin)
                    pickle.dump(xbin, handler_bin, pickle.HIGHEST_PROTOCOL)
                    nd6 += 1               
        handler_bin.close()
    f.close()

    Trie_mkfile_Title(TitleDataCPD)




