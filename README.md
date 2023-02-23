# Equipe: “The Walking Data”

Integrantes: Brenda Schussler e Pedro Rigon

## DESCRIÇÃO DO PROBLEMA


O surgimento e desenvolvimento das plataformas de streaming resultou também
em uma revolução no mercado das produções audiovisuais. Nesse ramo, a empresa norte
americana Netflix se tornou uma potência dominante e com isso filmes e séries têm
influenciado, cada vez mais, o imaginário coletivo da população. Dessa forma, justificado
pela sua relevância socioeconômica, o conjunto de dados que selecionamos para trabalhar
contém as séries e filmes disponíveis na Netflix (atualizado em junho de 2021), o qual foi
retirado do site do IMDB. Com isso, nossa aplicação trata-se de um catálogo com os
títulos da Netflix, sendo possível fazer classificação e pesquisas nestes dados de acordo
com filtros pré-estabelecidos.

## PROJETO DE ARQUIVOS:

Inicialmente, foi feita a organização (divisão) dos dados em arquivos, separando-
os de acordo com suas categorias. No arquivo principal (NetflixVideosDataCPD), o
id_imdb de cada título está associado aos ids das suas respectivas informações (language,
startYear, type, country, rankpop). Nos demais arquivos, os ids de cada uma das categorias estão associados as suas
respectivas informações, para que, quando feita a busca (filtragem) dos dados, as
informações coletadas a respeito de cada título sejam corretas.

## ORGANIZAÇÃO DOS ARQUIVOS:

A organização de arquivos foi baseada no modelo estrela, no qual há um arquivo
principal que contém chaves de índice de acesso ao conteúdo que se encontra em arquivos
auxiliares. Tal modelo foi aplicado devido a intensa repetição de dados que o DataBase
carregava consigo, afim de facilitar a normalização e compactação dos dados através da
remoção de dados repetidos ou inúteis e da sua padronização. Tais aspectos facilitam o
trabalho de filtragem de dados e aceleram a busca dos dados através de arquivos
armazenados em disco. Para transformar o DataBase em um modelo estrela, utilizamos o programa Power
BI do Windows que possui funções especificas para o tratamento de dados, como por
exemplo: remoção de termos redundantes e inválidos, ligação entre colunas e inserção de
índices nas colunas. Utilizando tais funções, moldamos nosso arquivo csv de entrada,
obtendo como resultado os dados no seguinte modelo estrela:

Desta forma, obtivemos 7 arquivos csv, sendo 1 deles o arquivo central
(NetflixVideosDataCPD), o qual possui apenas os índices de acesso às informações dos
demais arquivos, e os outros 6, contendo suas respectivas informações específicas
referenciadas pelo índice de acesso contido no arquivo csv principal.

```
Figura 1 : Modelo Estrela feito utilizando o Power BI.
```

Além disso, foram tratados alguns problemas de informação contidos nos dados
inicialmente extraídos, como:

- Espaço antes dos títulos;
- Letras maiúsculas;
- Letras desconfiguradas;
- Caracteres inválidos.

Para isso, utilizamos as próprias funções presentes no Excel, dentre elas
ARRUMAR1(coluna) e MAIÚSCULA(coluna), além disso, implementamos através do
modo desenvolvedor, uma função que remove, se existir na linha, caractere de <space>
no início do texto.

A figura 3 exemplifica como ficou estruturado o arquivo csv principal, sendo que
nele há apenas os índices de acesso às informações que se encontram nos outros arquivos,
de modo, que cada linha apresenta a informação relacionada com o id_title. Portanto,
cada linha carrega consigo índices de acesso à informação de um determinado título
presente no streaming Netflix.

```
Figura 3 : Arquivo Csv principal
```

Para a ligação desses arquivos foram criadas árvores trie como índice de acesso
ao arquivo principal. Há, árvores trie normais e invertidas, afim de facilitar o acesso,
aumentar a velocidade dos filtros de busca e diminuir o tempo de execução das filtragens.
Ao todo, foram criados os seguintes arquivos binários em forma de árvores trie:

## FUNCIONALIDADES DA APLICAÇÃO:

A aplicação é organizada em menus, que permitem que o usuário realize o que
desejar (dentre as funcionalidades disponíveis) com os dados trabalhados.

- Pesquisa de dados: ao selecionar a opção no menu principal, o usuário terá acesso ao menu de filtros, que permite fazer a pesquisa de dados de acordo com diversos filtros/categorias, conforme listados a seguir:
  1. Imdb_id: ao escolher essa opção, o usuário filtra a obra desejada buscando-a através do seu código de Imdb_id.
  2. Language: ao escolher essa opção, o usuário poderá buscar quais obras (dentre as contidas nos dados) tem como idioma original o digitado na busca do filtro. Por exemplo, ao filtrar por “french” a aplicação irá mostrar ao usuário quais os títulos possuem o idioma francês como idioma original.
  3. Popularity: essa opção permite ao usuário filtrar a obra de acordo com sua popularidade no ranking geral da Netflix. Por exemplo, ao buscar por “ 5 ” a aplicação irá apresentar ao usuário qual é o título que ocupa a quinta posição no ranking.
  4. Start Year: ao selecionar essa opção, o usuário deve inserir um ano, e em seguida a aplicação mostrará quais títulos tiveram sua data de estreia no respectivo ano buscado.
  5. Type: permite que o usuário busque quais as obras são do tipo buscado, sendo possível buscar as opções: tvseries, movie, tvspecial, tvminiseries, short, vídeo, tvmovie, tvshort, videogame, tvepisode.
  6. Origin Country: essa opção permite que o usuário filtre as obras de acordo com seu país de origem. Por exemplo, ao buscar por “Brazil” a aplicação apresentará quais os títulos têm “Brazil” como país de origem.

Também é possível fazer uma busca por prefixos no menu principal ao selecionar
a opção 1). Ou seja, escolhendo a primeira opção no menu principal, o usuário pode
pesquisar quais obras constam no catálogo tendo em seu título o prefixo pesquisado.
Por exemplo, ao buscar “the” a aplicação irá listar todos as obras que tem como
prefixo “the” em seus títulos. Ainda dentro desta opção, após a listagem dos títulos de
acordo com a filtragem de prefixo inserida, o usuário pode escolher um dos títulos da
lista para consultar todas as informações referentes a ele.

```
Figura 5 : Menu Principal
```
```
Figura 6 : Menu de Filtros buscando o título pelo seu imdb_id.
```

```
Figura 7 : Menu de Filtros buscando os títulos pelo idioma.
```
Figura 8 : Menu de Filtros buscando o título pela popularidade.


Figura 9 : Menu de Filtros buscando os títulos pelo ano de estreia.

```
Figura 10 : Menu de Filtros buscando os títulos pelo tipo.
```

Figura 11 : Menu de Filtros buscando os títulos pelo país de origem.


Figura 12 : Menu Principal buscando por prefixo e em seguida exibindo as informações do título
desejado dentre os listados com o respectivo prefixo.


- Ordenação dos dados: ao selecionar a opção 6) do menu, o usuário entra no menu
    de ordenação, que lhe permite ordenar os títulos de acordo com os seguintes critérios:
    Ordem Alfabética Normal, Ordem Alfabética Inversa, Ranking Popularidade em
    ordem normal, Ranking Popularidade em ordem inversa.

```
Figura 13 : Menu de Ordenação
```
```
Figura 14 : parte da ordenação em ordem alfabética normal
```

```
Figura 15 : parte da ordenação em ordem alfabética inversa.
```
Figura 16 : parte da ordenação pelo ranking em ordem normal.


Figura 17 : parte da ordenação pelo ranking em ordem inversa.


- Top 10: ao selecionar a opção 5) do menu principal, o usuário terá acesso ao menu
    Top 10, onde poderá listar os “Top 10” (primeiros 10 classificados de acordo com o
    ranking), de acordo com as categorias: Top 10 Filmes e Top 10 Series.

```
Figura 18 : menu Top 10 exibindo Top 10 Filmes.
```
```
Figura 19 : menu Top 10 exibindo Top 10 Series.
```

- Inserção e Remoção de dados: ao escolher a opção 3) do menu principal, o usuário
    poderá inserir uma nova obra no catálogo, assim como, ao escolher a opção 4) poderá
    excluir (remover) uma obra do catálogo.

## BIBLIOTECAS UTILIZADAS:

- pandas: está biblioteca foi utilizada para fazer a limpeza inicial dos dados, e para
    auxiliar na implementação das funções de inserção e remoção de um título ao
    catálogo. Além disso, foi utilizada para a coleta dos dados do arquivo csv para um
    arquivo binário.
- heapq: foi utilizada para auxiliar na implementação da função de ordenação dos
    dados (heapsort).
- pickle: esta biblioteca foi usada para serializar os dados contidos em um arquivo
    binário. Portanto, os dados eram armazenados e carregados usando essa função
    que servia como uma interface entre arquivo binário e programa, facilitando a
    extração e simplificando processos que poderiam ser feitos manualmente, porém
    trariam um nível de complexidade e de tempo maior frente ao objetivo do trabalho.
- csv: foi utilizado para facilitar a identificação e a conversão dos dados csv para
    arquivos binários, cria uma interface arquivo-programa que facilita a aplicação
    das funções e dos módulos responsáveis pela filtragem de dados.
- os: usado para a exclusão dos arquivos binários, quando novos arquivos são
    criados ao executar as funções de adicionar ou remover obra ao catálogo.

## COMO COMPILAR O CÓDIGO:

Após baixar o arquivo .zip ou .rar enviado, descompactar e abrir a pasta que se
encontra dentro do arquivo como projeto de alguma IDE configurada para Python3. Após
isso, basta executar o módulo main.py. Para percorrer as funcionalidades da aplicação
basta ir escolhendo as opções desejadas dos menus, explicadas em cada um deles.

```
python main.py
```
## CONSIDERAÇÕES FINAIS:


Se tivéssemos mais tempo, gostaríamos de aprimorar nossas funções de busca,
incrementando o número de filtros, bem como, encadeando-os, possibilitando ao usuário
buscar por mais de um filtro ao mesmo tempo. Também achamos que seria interessante
implementar uma árvore B para pesquisas por alguns filtros específicos, visando facilitar
o acesso ao arquivo principal, o que tornaria a filtragem um processo mais rápido e
eficiente. Além disso, era de nosso interesse corrigir alguns bugs específicos, como o que
obtivemos ao inserir um novo ano de estreia, sendo o único dado que não aceitou ser
inserido com valor diferente dos já existentes no arquivo, dentre outras limitações e
aprimoramentos de código que poderiam ter sido implementados.

