from CsvConverterBinary import *
from ArqProject import *
from structsArq import *
from Trie_mainBin import *
from Buscas_trie import *
import pandas as pd
import os
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


def print_menuOrdenacao():
    print("  ______________________________________________________________________________________________________________________ ")
    print(" |    __  __                             ___               _                                  ____                      | ")
    print(" |   |  \/  |   ___   _ __    _   _     / _ \   _ __    __| |   ___   _ __     __ _    ___    __ _    ___               | ")
    print(" |   | |\/| |  / _ \ | '_ \  | | | |   | | | | | '__|  / _` |  / _ \ | '_ \   / _` |  / __|  / _` |  / _ \              | ")
    print(" |   | |  | | |  __/ | | | | | |_| |   | |_| | | |    | (_| | |  __/ | | | | | (_| | | (__  | (_| | | (_) |             | ")
    print(" |   |_|  |_|  \___| |_| |_|  \__,_|    \___/  |_|     \__,_|  \___| |_| |_|  \__,_|  \___|  \__,_|  \___/              | ")
    print(" |                                                                                      |                               | ")
    print(" |______________________________________________________________________________________________________________________| ")
    print('-' * 20)
    print('Menu Interativo')
    print('-' * 20)
    print("Opcoes de Ordenacao: ")
    print("[1] - Titulos em ordem alfabética normal")
    print("[2] - Titulos em ordem alfabética inversa")
    print("[3] - Ranking de popularidade em ordem normal")
    print("[4] - Ranking de popularidade em ordem inversa")
    print("[5] - Sair do Menu de Ordenaçao")


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
    print("[5] - Top 10")
    print("[6] - Ordenar NetflixTvShows")
    print("[7] - Encerrar Programa")


def print_menuTopFilmes():
    print("  ______________________________________________________________________________")
    print(" |   __  __                            _____                     _    ___       | ")
    print(" |  |  \/  |   ___   _ __    _   _    |_   _|   ___    _ __     / |  / _ \      | ")
    print(" |  | |\/| |  / _ \ | '_ \  | | | |     | |    / _ \  | '_ \    | | | | | |     | ")
    print(" |  | |  | | |  __/ | | | | | |_| |     | |   | (_) | | |_) |   | | | |_| |     | ")
    print(" |  |_|  |_|  \___| |_| |_|  \__,_|     |_|    \___/  | .__/    |_|  \___/      | ")
    print(" |                                                    |_|                       | ")
    print(" |______________________________________________________________________________| ")
    print('-' * 20)
    print('Menu Interativo')
    print('-' * 20)
    print("Opcoes de Filtro: ")
    print("[1] - Filmes")
    print("[2] - Series")
    print("[3] - Sair do Menu de Top 10 Filmes")


def menuADDnovaObra():
    print("  _______________________________________________________________  ")
    print(" |   __  __                               _      ____    ____    | ")
    print(" |  |  \/  |   ___   _ __    _   _       / \    |  _ \  |  _ \   | ")
    print(" |  | |\/| |  / _ \ | '_ \  | | | |     / _ \   | | | | | | | |  | ")
    print(" |  | |  | | |  __/ | | | | | |_| |    / ___ \  | |_| | | |_| |  | ")
    print(" |  |_|  |_|  \___| |_| |_|  \__,_|   /_/   \_\ |____/  |____/   | ")
    print(" |_______________________________________________________________| ")
    print('-' * 20)
    print('Menu Interativo')
    print('-' * 20)
    print("[1] - Adicionar Nova Obra")
    print("[2] - Sair do Menu ADD ")


def menuRemoveObra():
    print("  ________________________________________________________________________________________ ")
    print(" |   __  __                             ____                                              | ")
    print(" |  |  \/  |   ___   _ __    _   _     |  _ \    ___   _ __ ___     ___   __   __   ___   | ")
    print(" |  | |\/| |  / _ \ | '_ \  | | | |    | |_) |  / _ \ | '_ ` _ \   / _ \  \ \ / /  / _ \  | ")
    print(" |  | |  | | |  __/ | | | | | |_| |    |  _ <  |  __/ | | | | | | | (_) |  \ V /  |  __/  | ")
    print(" |  |_|  |_|  \___| |_| |_|  \__,_|    |_| \_\  \___| |_| |_| |_|  \___/    \_/    \___|  | ")
    print(" |________________________________________________________________________________________| ")
    print('-' * 20)
    print('Menu Interativo')
    print('-' * 20)
    print("[1] - Remover Obra")
    print("[2] - Sair do Menu Remove ")


def MenuRemove():
    menu = '11'
    while menu != '2':
        menuRemoveObra()
        menu = (input("Sua opcao: "))
        if menu == '2':
            break
        elif menu == '1':
            FuncaoRemove()
        else:
            print()
            print("************************************************")
            print("Opcao invalida (Atencao para as opcoes do menu!)")
            print("************************************************")
            pass


def FuncaoRemove():

    titulo_delete = input("Qual o título que deseja remover do arquivo? ")
    test1 = Busca_id_title(titulo_delete)
    if test1 != False:
        df = pd.read_csv(r"src\csv\TitleDataCPD.csv")

        id_title_delete = []
        # esse for pega o id do titulo que desejo deletar
        for n, line in df.iterrows():
            if titulo_delete == line['title']:
                id_title_delete.append(line['id_imdbtitle'])

        # indexName recebe o indice do id que desejamos deletar
        for i in id_title_delete:
            indexName = df[df['id_imdbtitle'] == i].index
            # drop deleta a linha
            df.drop(indexName, inplace=True)

        # cria arquivo de Title data com o titulo deletado
        df.to_csv(r"src\csv\TitleDataCPD.csv", index=False)

        # agora deletar do arquivo de data geral
        df = pd.read_csv(r"src\csv\NetflixVideosDataCPD.csv")

        id_ranking_delete = []
        # esse for pega o id do titulo que desejo deletar
        for n, line in df.iterrows():
            for i in id_title_delete:
                if i == line['id_imdbtitle']:
                    id_ranking_delete.append(line['id_rankpop'])
                    # indexName recebe o indice do id que desejamos deletar
                    indexName = df[df['id_imdbtitle'] == i].index
                    # drop deleta a linha
                    df.drop(indexName, inplace=True)

        # cria arquivo de Data data com o titulo deletado
        df.to_csv(r"src\csv\NetflixVideosDataCPD.csv", index=False)

        # agora deletar no arquivo do ranking
        df = pd.read_csv(r"src\csv\PopularRankDataCPD.csv")

        # esse for pega o id do titulo que desejo deletar
        for n, line in df.iterrows():
            for i in id_ranking_delete:
                if i == line['popular_rank']:
                    # indexName recebe o indice do id que desejamos deletar
                    indexName = df[df['id_rankpop'] == i].index
                    # drop deleta a linha
                    df.drop(indexName, inplace=True)

        # cria arquivo de Title data com o titulo deletado
        df.to_csv(r"src\csv\PopularRankDataCPD.csv", index=False)

        os.remove(r"src\bin\NetflixVideosDataCPD.bin")
        os.remove(r"src\bin\CabecalhoPrincipal.bin")
        os.remove(r"src\bin\country_trieinvertido.bin")
        os.remove(r"src\bin\country_trie.bin")
        os.remove(r"src\bin\language_trie.bin")
        os.remove(r"src\bin\language_trieinvertido.bin")
        os.remove(r"src\bin\netflix_trie.bin")
        os.remove(r"src\bin\rankpop_trie.bin")
        os.remove(r"src\bin\rankpop_trieinvertido.bin")
        os.remove(r"src\bin\styear_styear.bin")
        os.remove(r"src\bin\styear_styearinvertido.bin")
        os.remove(r"src\bin\title_trie.bin")
        os.remove(r"src\bin\title_trieinvertido.bin")
        os.remove(r"src\bin\type_trie.bin")
        os.remove(r"src\bin\type_trieinvertido.bin")

        CsvtoBin()
    else:
        print("Obra nao encontrada do DataBase!")


def MenuADD():
    menu = '11'
    while menu != '2':
        menuADDnovaObra()
        menu = (input("Sua opcao: "))
        if menu == '2':
            break
        elif menu == '1':
            ADD_Obra()
            #print("Implementar ADD")
        else:
            print()
            print("************************************************")
            print("Opcao invalida (Atencao para as opcoes do menu!)")
            print("************************************************")
            pass


def ADD_Obra():
    # TITULO
    titulo_add = input("Qual o título que deseja adicionar ao arquivo? ")
    test2 = Busca_id_title(titulo_add)
    if test2 == False:

        df = pd.read_csv(r"src\csv\TitleDataCPD.csv")

        # Cria novo Id_title para esse novo titulo
        cont_id = len(df.index)
        id = 9916362 + cont_id
        id = str(id)
        new_id = "tt" + id
        dados1 = {'id_imdbtitle': new_id, 'title': titulo_add}
        df1 = pd.DataFrame(dados1, index=[len(df.index)])
        frames = [df, df1]
        df = pd.concat(frames)

        # cria arquivo de Title data com o titulo adicionado
        df.to_csv(r"src\csv\TitleDataCPD.csv", index=False)

        # COUNTRY
        country_add = input(
            "Qual o país de origem do título que deseja adicionar ao arquivo? ")

        df = pd.read_csv(r"src\csv\CountryOriginDataCPD.csv")

        flag_country = 0
        # esse for pega o id do country
        for n, line in df.iterrows():
            if country_add == line['orign_country']:
                id_country_add = (line['id_orign'])
                flag_country = 1

        if flag_country == 0:
            new_id_country = (len(df.index)) + 1
            new_id_country = str(new_id_country)
            dados5 = {'id_orign': new_id_country, 'orign_country': country_add}
            df5 = pd.DataFrame(dados5, index=[len(df.index)])
            frames = [df, df5]
            df = pd.concat(frames)
            id_country_add = new_id_country
            df.to_csv(r"src\csv\CountryOriginDataCPD.csv", index=False)

        # LANGUAGE
        language_add = input(
            "Qual o idioma do título que deseja adicionar ao arquivo? ")

        df = pd.read_csv(r"src\csv\LanguageDataCPD.csv")

        flag_language = 0
        # esse for pega o id de language
        for n, line in df.iterrows():
            if language_add == line['language']:
                id_language_add = (line['id_language'])
                flag_language = 1

        if flag_language == 0:
            new_id_language_add = (len(df.index)) + 1
            new_id_language_add = str(new_id_language_add)
            dados5 = {'id_language': new_id_language_add,
                      'language': language_add}
            df5 = pd.DataFrame(dados5, index=[len(df.index)])
            frames = [df, df5]
            df = pd.concat(frames)
            id_language_add = new_id_language_add
            df.to_csv(r"src\csv\LanguageDataCPD.csv", index=False)

        # START YEAR
        repet = 1
        while repet == 1:
            year_add = input("Qual o ano de estreia do título que deseja adicionar ao arquivo? ")
            id_year_add = Busca_id_styear(year_add)
            if id_year_add == False:
                repet = 1
                print("Digite um ano valido!")
            else:
                repet = 0

        # TYPE
        type_add = input(
            "Qual o tipo do título que deseja adicionar ao arquivo? \n opções: tvSeries\n movie\n tvSpecial\n tvMiniSeries\n short\n video\n tvMovie\n tvShort\n videoGame\n tvEpisode\n\n ")

        df = pd.read_csv(r"src\csv\TypeDataCPD.csv")

        # esse for pega o id do type
        for n, line in df.iterrows():
            if type_add == line['type']:
                id_type_add = (line['id_type'])

        # RANKING
        contRank = 1  # VER ONDE INICIALIZAR
        df = pd.read_csv(r"src\csv\PopularRankDataCPD.csv")

        new_rank = len(df.index) + contRank
        id_rank_add = new_rank

        dados2 = {'id_rankpop': id_rank_add, 'popular_rank': new_rank}
        df1 = pd.DataFrame(dados2, index=[len(df.index)])
        frames = [df, df1]
        df = pd.concat(frames)

        df.to_csv(r"src\csv\PopularRankDataCPD.csv", index=False)

        df = pd.read_csv(r"src\csv\NetflixVideosDataCPD.csv")

        dados3 = {'id_imdbtitle': new_id, 'id_languages': id_language_add, 'id_styear': id_year_add,
                  'id_type': id_type_add, 'id_country': id_country_add, 'id_rankpop': id_rank_add}
        df3 = pd.DataFrame(dados3, index=[len(df.index)])
        frames = [df, df3]
        df = pd.concat(frames)

        # cria arquivo de Title data com o titulo adicionado
        df.to_csv(r"src\csv\NetflixVideosDataCPD.csv", index=False)
        os.remove(r"src\bin\NetflixVideosDataCPD.bin")
        os.remove(r"src\bin\CabecalhoPrincipal.bin")
        os.remove(r"src\bin\country_trieinvertido.bin")
        os.remove(r"src\bin\country_trie.bin")
        os.remove(r"src\bin\language_trie.bin")
        os.remove(r"src\bin\language_trieinvertido.bin")
        os.remove(r"src\bin\netflix_trie.bin")
        os.remove(r"src\bin\rankpop_trie.bin")
        os.remove(r"src\bin\rankpop_trieinvertido.bin")
        os.remove(r"src\bin\styear_styear.bin")
        os.remove(r"src\bin\styear_styearinvertido.bin")
        os.remove(r"src\bin\title_trie.bin")
        os.remove(r"src\bin\title_trieinvertido.bin")
        os.remove(r"src\bin\type_trie.bin")
        os.remove(r"src\bin\type_trieinvertido.bin")

        CsvtoBin()
    else:
        print("Obra ja se encontra no DataBase!")


def OrdenarObras():
    menu = '11'
    while menu != '7':
        print_menuOrdenacao()
        menu = (input("Sua opcao: "))
        if menu == '5':
            break
        elif menu == '1':
            OrdenarObrasTituloNormal()
        elif menu == '2':
            OrdenarObrasTituloInverso()
        elif menu == '3':
            OrdenarObrasRankNormal()
        elif menu == '4':
            OrdenarObrasRankInverso()
            pass
        else:
            print()
            print("**")
            print("Opcao invalida (Atencao para as opcoes do menu!)")
            print("**")
            pass


def OrdenarObrasTituloNormal():
    lista_titulos = []
    prefix = ""
    lista_titulos = Busca_filmePrefix(prefix)
    vet = heapsort(lista_titulos)

    print("Lista de Títulos Ordenada em Ordem Alfabetica: ")
    print()
    for i in vet:
        print(i)
    print()


def OrdenarObrasTituloInverso():
    lista_titulos = []
    prefix = ""
    lista_titulos = Busca_filmePrefix(prefix)
    vet = heapsort(lista_titulos)

    print("Lista de Títulos Ordenada em Ordem Alfabetica Inversa: ")
    print()
    for i in reversed(vet):
        print(i)
    print()


def OrdenarObrasRankNormal():
    title_list = []
    for i in range(1, 101):
        title = PopularidadeFiltro(i)
        title_list.append(title)
    n = 1
    print()
    print("Exibindo 100 titulos mais populares em ordem crescente de popularidade:")
    print()
    for i in title_list:
        print(n, ":", i)
        n = n + 1


def OrdenarObrasRankInverso():
    title_list = []
    for i in range(1, 101):
        title = PopularidadeFiltro(i)
        title_list.append(title)
    n = 100
    print()
    print("Exibindo 100 titulos mais populares em ordem decrescente de popularidade:")
    print()
    for i in reversed(title_list):
        print(n, ":", i)
        n = n-1


def heapsort(iterable):
    aux = []
    for title in iterable:
        heapq.heappush(aux, title)
    return [heapq.heappop(aux) for i in range(len(aux))]


def BuscarObras():
    prefix = input("Digite o prefixo para Busca: ")
    prefix = prefix.lower()
    list_titles = Busca_filmePrefix(prefix)
    if len(list_titles) == 0:
        print()
        print("Nada foi encontrado no DataBase :c")
        print()
    else:
        print()
        print("Foram encontrados as seguintes obras no DataBase:")
        print()
        vet = heapsort(list_titles)
        #t = time.process_time() - tempo
        for i in range(len(vet)):
            print(f"{i+1}) {vet[i]}")
        print()
        n = (input("Digite o numero da obra que deseja obter informações: "))
        n = int(n)
        n = n - 1
        Catalogo(vet, n)


def BuscarObrasfilto1():
    id_title = input("Digite o imdb_id: ")
    id_title = id_title.lower()
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
    linguagem = linguagem.lower()
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
        vet = heapsort(list_title)
        for i in vet:
            print(i)
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
        vet = heapsort(list_title)
        for i in vet:
            print(i)
        print()


def BuscarObrasfilto5():
    list_title = []
    print()
    print("Tipos de Obras Disponiveis:")
    print("- tvseries")
    print("- movie")
    print("- tvspecial")
    print("- tvminiseries")
    print("- short")
    print("- video")
    print("- tvmovie")
    print("- tvshort")
    print("- videogame")
    print("- tvepisode")
    print()
    # Colocar os tipos dispiniveis para busca
    type = input("Digite o Tipo de Obra: ")
    type = type.lower()
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
        vet = heapsort(list_title)
        for i in vet:
            print(i)
        print()


def BuscarObrasfilto6():
    list_title = []
    country = input("Digite o Pais de Origem: ")
    country = country.lower()
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
        vet = heapsort(list_title)
        for i in vet:
            print(i)
        print()


def BuscarObrasPais():
    list_title = []
    country = input("Digite o Pais de Origem: ")
    country = country.lower()
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


def PopularidadeFiltro(id_rankpop):
    list_title = []
    id_rankpop = str(id_rankpop)
    list_id_title = Busca_id_titleporid_rankpop(id_rankpop)
    if list_id_title != False:
        for i in list_id_title:
            title = Busca_title(i)
            return title
    else:
        title = False
        return title


def Top10Filmes_rank():
    print("Buscando Top 10 Filmes Aclamados pela Critica")
    print("...")
    print("")
    modelo = open(r"src\bin\CabecalhoPrincipal.bin", "rb")
    inf = pickle.load(modelo)
    modelo.close()
    lenrank = inf.nd
    lenrank = lenrank + 1
    cont = 0
    title_list = []
    for i in range(lenrank):
        if i != 0:
            title = PopularidadeFiltro(i)
            if title != False:
                id_title = Busca_id_title(title)
                #confirm = id_title_eh_movie(id_title)
                resp = Busca_id_type_por_id_title(id_title)
                if resp == "2":
                    title_list.append(title)
                    cont += 1
                    if(cont == 10):
                        return title_list
    return title_list


def Top10Series_rank():
    print("Buscando Top 10 Series Aclamadas pela Critica")
    print("...")
    print("")
    modelo = open(r"src\bin\CabecalhoPrincipal.bin", "rb")
    inf = pickle.load(modelo)
    modelo.close()
    lenrank = inf.nd
    lenrank = lenrank + 1
    cont = 0
    title_list = []
    for i in range(lenrank):
        if i != 0:
            title = PopularidadeFiltro(i)
            if title != False:
                id_title = Busca_id_title(title)
                #confirm = id_title_eh_movie(id_title)
                resp = Busca_id_type_por_id_title(id_title)
                if resp == "1":
                    title_list.append(title)
                    cont += 1
                    if(cont == 10):
                        return title_list
    return title_list


def Top10Filmes():
    menu = '11'
    while menu != '7':
        print_menuTopFilmes()
        menu = (input("Sua opcao: "))
        if menu == '3':
            break
        elif menu == '1':
            title1 = Top10Filmes_rank()
            if len(title1) == 0:
                print("Nenhum filme encontrado!")
            else:
                for i in range(len(title1)):
                    print(f"{i+1}) {title1[i]}")
        elif menu == '2':
            title2 = Top10Series_rank()
            if len(title2) == 0:
                print("Nenhum filme encontrado!")
            else:
                for i in range(len(title2)):
                    print(f"{i+1}) {title2[i]}")
        else:
            print()
            print("************************************************")
            print("Opcao invalida (Atencao para as opcoes do menu!)")
            print("************************************************")
            pass


def FiltrarObras():
    menu = '11'
    while menu != '7':
        print_menufiltro()
        menu = (input("Sua opcao: "))
        if menu == '7':
            break
        elif menu == '1':
            BuscarObrasfilto1()
        elif menu == '2':
            BuscarObrasfilto2()
        elif menu == '3':
            BuscarObrasfilto3()
        elif menu == '4':
            BuscarObrasfilto4()
        elif menu == '5':
            BuscarObrasfilto5()
        elif menu == '6':
            BuscarObrasfilto6()
            pass
        else:
            print()
            print("************************************************")
            print("Opcao invalida (Atencao para as opcoes do menu!)")
            print("************************************************")
            pass


def Catalogo(vetor, offset):
    title = vetor[offset]
    id_title = Busca_id_title(title)
    id_language = Busca_id_languages_por_id_title(id_title)
    id_styear = Busca_id_styear_por_id_title(id_title)
    id_type = Busca_id_type_por_id_title(id_title)
    id_country = Busca_id_country_por_id_title(id_title)
    id_rankpop = Busca_id_rankpop_por_id_title(id_title)
    language = Busca_languages(id_language)
    st_year = Busca_styear(id_styear)
    type = Busca_type(id_type)
    country = Busca_country(id_country)
    rankpop = Busca_rankpop(id_rankpop)
    print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print(f"TITULO DA OBRA: {title.upper()}")
    print(f"LINGUAGEM ORIGINAL: {language.upper()}")
    print(f"ANO DE ESTREIA: {st_year}")
    print(f"TIPO DE OBRA: {type.upper()}")
    print(f"PAIS DE ORIGEM: {country.upper()}")
    print(f"RANKING DE POPULARIDADE ENTRE USUARIOS DA NETFLIX: {rankpop}")
    print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")


def switchMainmenu():
    menu = '11'
    while menu != '7':
        exibirmenu()
        menu = (input("Sua opcao: "))
        if menu == '7':
            break
        elif menu == '1':
            BuscarObras()
        elif menu == '2':
            FiltrarObras()
        elif menu == '3':
            MenuADD()
        elif menu == '4':
            MenuRemove()
        elif menu == '5':
            Top10Filmes()
        elif menu == '6':
            OrdenarObras()
        else:
            print()
            print("************************************************")
            print("Opcao invalida (Atencao para as opcoes do menu!)")
            print("************************************************")
            pass
