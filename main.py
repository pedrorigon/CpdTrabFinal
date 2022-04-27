from CsvConverterBinary import *
from ArqProject import *
from structsArq import *
from Trie_mainBin import *
from Buscas_trie import *


def artepython():
    print("  ____________________________________________________________________________________________________________________________ ")
    print(" |   _____                  _               _   _                 _____   _                   _        ____   ____    ____    |")
    print(" |  |_   _|  _ __    __ _  | |__     __ _  | | | |__     ___     |  ___| (_)  _ __     __ _  | |      / ___| |  _ \  |  _ \   |")
    print(" |    | |   | '__|  / _` | | '_ \   / _` | | | | '_ \   / _ \    | |_    | | | '_ \   / _` | | |     | |     | |_) | | | | |  |")
    print(" |    | |   | |    | (_| | | |_) | | (_| | | | | | | | | (_) |   |  _|   | | | | | | | (_| | | |     | |___  |  __/  | |_| |  |")
    print(" |    |_|   |_|     \__,_| |_.__/   \__,_| |_| |_| |_|  \___/    |_|     |_| |_| |_|  \__,_| |_|      \____| |_|     |____/   |")
    print(" |____________________________________________________________________________________________________________________________|")


def exibirmenu():
    menu = 1
    while menu != 5:
        print('-' * 20)
        print('Menu Interativo')
        print('-' * 20)
        print("Opcoes: ")
        print("[1] - Buscar NetflixTvShows")
        print("[2] - Inserir Obra")
        print("[3] - Remover Obra")
        print("[2] - Top 10 Filmes")
        print("[3] - top 10 Series")
        print("[4] - Ordenar NetflixTvShows")
        print("[5] - Encerrar Programa")

        menu = int(input("Sua opcao: "))
        if menu == 5:
            break
        elif menu == 1:
            prefix = input("Digite o prefixo para Busca: ")
            list_titles = Busca_filmePrefix(prefix)
            if len(list_titles) == 0:
                print("Nada foi encontrado no DataBase :c")
            else:
                print("Foram encontrados as seguintes obras no DataBase:")
                for i in list_titles:
                    print(i)
        elif menu == 2:
            pass
        elif menu == 3:
            pass
        elif menu == 4:
            pass
        else:
            print("Opcao invalida (Atencao para as opcoes do menu!")
            pass

#CsvtoBin()
artepython()
exibirmenu()