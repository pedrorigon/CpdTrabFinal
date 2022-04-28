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

def print_menuTopFilmes():
    print("  ______________________________________________________________________________________________________________________ ")
    print(" |   __  __                            _____                     _    ___      _____   _   _                            | ")
    print(" |  |  \/  |   ___   _ __    _   _    |_   _|   ___    _ __     / |  / _ \    |  ___| (_) | |  _ __ ___     ___   ___   | ")
    print(" |  | |\/| |  / _ \ | '_ \  | | | |     | |    / _ \  | '_ \    | | | | | |   | |_    | | | | | '_ ` _ \   / _ \ / __|  | ")
    print(" |  | |  | | |  __/ | | | | | |_| |     | |   | (_) | | |_) |   | | | |_| |   |  _|   | | | | | | | | | | |  __/ \___   | ")
    print(" |  |_|  |_|  \___| |_| |_|  \__,_|     |_|    \___/  | .__/    |_|  \___/    |_|     |_| |_| |_| |_| |_|  \___| |___/  | ")
    print(" |                                                    |_|                                                               | ")
    print(" |______________________________________________________________________________________________________________________| ")
    print('-' * 20)
    print('Menu Interativo')
    print('-' * 20)
    print("Opcoes de Filtro: ")
    print("[1] - Geral")
    print("[2] - Por Pais")
    print("[3] - Mais Recentes")
    print("[4] - Mais Antigos")
    print("[5] - Sair do Menu de Top 10 Filmes")


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
    list_title = []
    linguagem = input("Digite a linguagem: ")
    id_linguagem = Busca_id_languages(linguagem)
    if id_linguagem == False:
        print()
        print("Nada foi encontrado no DataBase :c")
        print()
    else:
        id_linguagem = str(id_linguagem)
        list_id_title = Busca_id_titleporid_language(id_linguagem)
        for i in list_id_title:
            title = Busca_title(i)
            list_title.append(title)
        print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")
        print("Foram encontrados as seguintes obras no DataBase:")
        print("'''''''''''''''''''''''''''''''''''''''''''''''''")
        tempo = time.process_time()
        vet = heapsort(list_title)
        for i in vet:
            print(i)
        t = time.process_time() - tempo 
        print()
        print(f"A ordenação em ordem alfabética levou {t} segundos")
        print()

def BuscarObrasfilto3():
    list_title = []
    rankpop = input("Digite a Popularidade: ")
    rankpop = str(rankpop)
    id_rankpop = Busca_id_rankpop(rankpop)
    if id_rankpop == False:
        print()
        print("Nada foi encontrado no DataBase :c")
        print()
    else:
        id_rankpop = str(id_rankpop)
        list_id_title = Busca_id_titleporid_rankpop(id_rankpop)
        for i in list_id_title:
            title = Busca_title(i)
            list_title.append(title)
        print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")
        print("Foram encontrados as seguintes obras no DataBase:")
        print("'''''''''''''''''''''''''''''''''''''''''''''''''")
        tempo = time.process_time()
        for i in list_title:
            print(i)
        print()


def BuscarObrasfilto4():
    list_title = []
    styear = input("Digite o Ano de Estreia: ")
    id_styear = Busca_id_styear(styear)
    if id_styear == False:
        print()
        print("Nada foi encontrado no DataBase :c")
        print()
    else:
        id_styear = str(id_styear)
        list_id_title = Busca_id_titleporid_styear(id_styear)
        for i in list_id_title:
            title = Busca_title(i)
            list_title.append(title)
        print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")
        print("Foram encontrados as seguintes obras no DataBase:")
        print("'''''''''''''''''''''''''''''''''''''''''''''''''")
        tempo = time.process_time()
        vet = heapsort(list_title)
        for i in vet:
            print(i)
        t = time.process_time() - tempo 
        print()
        print(f"A ordenação em ordem alfabética levou {t} segundos")
        print()
    
def BuscarObrasfilto5():
    list_title = []
    type = input("Digite o Ano de Estreia: ")
    id_type = Busca_id_type(type)
    if id_type == False:
        print()
        print("Nada foi encontrado no DataBase :c")
        print()
    else:
        id_type = str(id_type)
        list_id_title = Busca_id_titleporid_type(id_type)
        for i in list_id_title:
            title = Busca_title(i)
            list_title.append(title)
        print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")
        print("Foram encontrados as seguintes obras no DataBase:")
        print("'''''''''''''''''''''''''''''''''''''''''''''''''")
        tempo = time.process_time()
        vet = heapsort(list_title)
        for i in vet:
            print(i)
        t = time.process_time() - tempo 
        print()
        print(f"A ordenação em ordem alfabética levou {t} segundos")
        print()

def BuscarObrasfilto6():
    list_title = []
    country = input("Digite o Pais de Origem: ")
    id_country = Busca_id_country(country)
    if id_country == False:
        print()
        print("Nada foi encontrado no DataBase :c")
        print()
    else:
        id_country = str(id_country)
        list_id_title = Busca_id_titleporid_country(id_country)
        for i in list_id_title:
            title = Busca_title(i)
            list_title.append(title)
        print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")
        print("Foram encontrados as seguintes obras no DataBase:")
        print("'''''''''''''''''''''''''''''''''''''''''''''''''")
        tempo = time.process_time()
        vet = heapsort(list_title)
        for i in vet:
            print(i)
        t = time.process_time() - tempo 
        print()
        print(f"A ordenação em ordem alfabética levou {t} segundos")
        print()

def BuscarObrasPais():
    list_title = []
    country = input("Digite o Pais de Origem: ")
    id_country = Busca_id_country(country)
    if id_country == False:
        print()
        print("Nada foi encontrado no DataBase :c")
        print()
    else:
        id_country = str(id_country)
        list_id_title = Busca_id_titleporid_country(id_country)
        for i in list_id_title:
            title = Busca_title(i)
            list_title.append(title)
    return list_title


def PopularidadeFiltro(rankpop):
    list_title = []
    rankpop = str(rankpop)
    id_rankpop = Busca_id_rankpop(rankpop)
    if id_rankpop == False:
        print()
        print("Nada foi encontrado no DataBase :c")
        print()
    else:
        id_rankpop = str(id_rankpop)
        list_id_title = Busca_id_titleporid_rankpop(id_rankpop)
        for i in list_id_title:
            title = Busca_title(i)
        tempo = time.process_time()
        return title

def Top10Filmes_rank():
    print("Buscando 10 melhores filmes aclamados")
    print("...")
    print("")
    lenrank = 7008
    cont = 0
    title_list = []
    for i in range(lenrank):
        if i != 0:
            title = PopularidadeFiltro(i)
            id_title = Busca_id_title(title)
            #confirm = id_title_eh_movie(id_title)
            resp = Busca_id_type_por_id_title(id_title)
            if resp == "2":
                title_list.append(title)
                cont += 1
                if(cont == 10):
                    return title_list

    return title_list

def Top10Filmes_pais():
    filme_Br = []
    title_list = BuscarObrasPais()
    for i in range(len(title_list)):
        id_title = Busca_id_title(title_list[i])
        id_type = Busca_id_type_por_id_title(id_title)
        id_type = str(id_type)
        if id_type == "2":
            filme_Br.append(title_list[i])
    
    return filme_Br

def Top10Filmes():
    menu = 11
    while menu != 7:
        print_menuTopFilmes()
        menu = int(input("Sua opcao: "))
        if menu == 5:
            break
        elif menu == 1:
            title1 = Top10Filmes_rank()
            if len(title1) == 0:
                print("Nenhum filme encontrado!")
            else:
                for i in range(len(title1)):
                    print(f"{i+1}) {title1[i]}")              
        elif menu == 2:
            title2 = Top10Filmes_pais()
            if len(title2) == 0:
                print("Nenhum filme encontrado!")
            else:
                for i in range(len(title2)):
                    print(f"{i+1}) {title2[i]}")   
        elif menu == 3:
            pass
        elif menu == 4:
            pass
        else:
            print()
            print("************************************************")
            print("Opcao invalida (Atencao para as opcoes do menu!)")
            print("************************************************")
            pass


def FiltrarObras():
    menu = 11
    while menu != 7:
        print_menufiltro()
        menu = int(input("Sua opcao: "))
        if menu == 7:
            break
        elif menu == 1:
            BuscarObrasfilto1()
        elif menu == 2:
            BuscarObrasfilto2()
        elif menu == 3:
            BuscarObrasfilto3()
        elif menu == 4:
            BuscarObrasfilto4()
        elif menu == 5:
            BuscarObrasfilto5()
        elif menu == 6:
            BuscarObrasfilto6()
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
            FiltrarObras()
        elif menu == 3:
            pass
        elif menu == 4:
            pass
        elif menu == 5:
            Top10Filmes()
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