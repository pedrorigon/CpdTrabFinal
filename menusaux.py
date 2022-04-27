from CsvConverterBinary import *
from ArqProject import *
from structsArq import *
from Trie_mainBin import *
from Buscas_trie import *
import time
import heapq

def artepython():
    print("  ____________________________________________________________________________________________________________________________ ")
    print(" |   _____                  _               _   _                 _____   _                   _        ____   ____    ____    |")
    print(" |  |_   _|  _ __    __ _  | |__     __ _  | | | |__     ___     |  ___| (_)  _ __     __ _  | |      / ___| |  _ \  |  _ \   |")
    print(" |    | |   | '__|  / _` | | '_ \   / _` | | | | '_ \   / _ \    | |_    | | | '_ \   / _` | | |     | |     | |_) | | | | |  |")
    print(" |    | |   | |    | (_| | | |_) | | (_| | | | | | | | | (_) |   |  _|   | | | | | | | (_| | | |     | |___  |  __/  | |_| |  |")
    print(" |    |_|   |_|     \__,_| |_.__/   \__,_| |_| |_| |_|  \___/    |_|     |_| |_| |_|  \__,_| |_|      \____| |_|     |____/   |")
    print(" |____________________________________________________________________________________________________________________________|")
    print("________________________________________________")
    print()
    print("Desenvolido por Brenda Schussler e Pedro Rigon")
    print("________________________________________________")

def print_menufiltro():
    print(" __________________________________________________________________________________________________  ")
    print(" |   __  __                                _            _____   _   _   _                          | ")
    print(" |  |  \/  |   ___   _ __    _   _      __| |   ___    |  ___| (_) | | | |_   _ __    ___    ___   | ")
    print(" |  | |\/| |  / _ \ | '_ \  | | | |    / _` |  / _ \   | |_    | | | | | __| | '__|  / _ \  / __|  | ")
    print(" |  | |  | | |  __/ | | | | | |_| |   | (_| | |  __/   |  _|   | | | | | |_  | |    | (_) | \__    | ")
    print(" |  |_|  |_|  \___| |_| |_|  \__,_|    \__,_|  \___|   |_|     |_| |_|  \__| |_|     \___/  |___/  | ")
    print(" |_________________________________________________________________________________________________| ")
    print('-' * 20)
    print('Menu Interativo')
    print('-' * 20)
    print("Buscar filme através do filtro: ")
    print("[1] - Imdb_id ")
    print("[2] - Language")
    print("[3] - Popularity")
    print("[4] - Start Year ")
    print("[5] - Type")
    print("[6] - Origin Country")
    print("[7] - Sair do menu de filtros")

def exibirmenu():
    print(" ___________________________________________________________________________________________________  ")
    print(" |    __  __                              ____           _                  _                   _   | ")
    print(" |   |  \/  |   ___   _ __    _   _      |  _ \   _ __  (_)  _ __     ___  (_)  _ __     __ _  | |  | ")
    print(" |   | |\/| |  / _ \ | '_ \  | | | |     | |_) | | '__| | | | '_ \   / __| | | | '_ \   / _` | | |  | ")
    print(" |   | |  | | |  __/ | | | | | |_| |     |  __/  | |    | | | | | | | (__  | | | |_) | | (_| | | |  | ")
    print(" |   |_|  |_|  \___| |_| |_|  \__,_|     |_|     |_|    |_| |_| |_|  \___| |_| | .__/   \__,_| |_|  | ")
    print(" |                                                                             |_|                  | ")
    print(" |__________________________________________________________________________________________________| ")
    print('-' * 20)
    print('Menu Interativo')
    print('-' * 20)
    print("Opcoes: ")
    print("[1] - Buscar NetflixTvShows")
    print("[2] - Filtrar Obra")
    print("[3] - Inserir Obra")
    print("[4] - Remover Obra")
    print("[5] - Top 10 Filmes")
    print("[6] - top 10 Series")
    print("[7] - Ordenar NetflixTvShows")
    print("[8] - Encerrar Programa")


def heapsort(iterable):
    aux = []
    for title in iterable:
        heapq.heappush(aux, title)
    return [heapq.heappop(aux) for i in range(len(aux))]


def BuscarObras():
    prefix = input("Digite o prefixo para Busca: ")
    list_titles = Busca_filmePrefix(prefix)
    if len(list_titles) == 0:
        print()
        print("Nada foi encontrado no DataBase :c")
        print()
    else:
        print()
        print("Foram encontrados as seguintes obras no DataBase:")
        print()
        tempo = time.process_time()
        vet = heapsort(list_titles)
        #t = time.process_time() - tempo    
        for i in vet:
            print(i)
        t = time.process_time() - tempo 
        print(f"Tempo de Execução: {t}")
        print(f"A ordenação em ordem alfabética levou {t} segundos")
        print()

def BuscarObrasfilto1():
    id_title = input("Digite o imdb_id: ")
    list_titles = Busca_title(id_title)
    if list_titles == False:
        print()
        print("Nada foi encontrado no DataBase :c")
        print()
    else:
        print()
        print("Foram encontrados as seguintes obras no DataBase:")
        print()
        print(list_titles)
        print()

def BuscarObrasfilto2():
    linguagem = input("Digite a linguagem: ")
    id_linguagem = Busca_id_languages(linguagem)
    if len(id_linguagem) == 0:
        print()
        print("Nada foi encontrado no DataBase :c")
        print()
    #else:
        ## fazer invertido no principal também
        #print()
        #print("Foram encontrados as seguintes obras no DataBase:")
       # print()
       # for i in list_titles:
            #print(i)
        #print()

def FiltrarObras():
    menu = 11
    while menu != 7:
        menu = int(input("Sua opcao: "))
        if menu == 8:
            break
        elif menu == 1:
            BuscarObrasfilto1()
        elif menu == 2:
            pass
        elif menu == 3:
            pass
        elif menu == 4:
            pass
        elif menu == 5:
            pass
        elif menu == 6:
            pass
        elif menu == 7:
            pass
        else:
            print()
            print("************************************************")
            print("Opcao invalida (Atencao para as opcoes do menu!)")
            print("************************************************")
            pass

def switchMainmenu():
    menu = 11
    while menu != 8:
        exibirmenu()
        menu = int(input("Sua opcao: "))
        if menu == 8:
            break
        elif menu == 1:
            BuscarObras()
        elif menu == 2:
            print_menufiltro()
            FiltrarObras()
        elif menu == 3:
            pass
        elif menu == 4:
            pass
        elif menu == 5:
            pass
        elif menu == 6:
            pass
        elif menu == 7:
            pass
        else:
            print()
            print("************************************************")
            print("Opcao invalida (Atencao para as opcoes do menu!)")
            print("************************************************")
            pass