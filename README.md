<h1>CPD Trabalho Final - Netflix Movies</h1>

> Trabalho Final Disciplina CPD - UFRGS 2021/2

### O surgimento e desenvolvimento das plataformas de streaming resultou também em uma revolução no mercado das produções audiovisuais. Nesse ramo, a empresa norte americana Netflix se tornou uma potência dominante e com isso filmes e séries cada vez mais tem influenciado o imaginário coletivo da população. Dessa forma, justificado pela importância socioeconômica, o conjunto de dados que selecionamos para trabalhar contém as séries e filmes disponíveis na Netflix (atualizado em junho de 2021), o qual foi retirado do site do IMDB.  Com isso, nossa aplicação deve possibilitar ao usuário ordenar os dados de acordo com alguns critérios (filtros) pré-selecionados bem como gerar top 10 filmes e/ou séries de acordo com alguns critérios (filtros) pré-selecionados. Para isso devemos seguir alguns passos para que chegamos à resolução dos problemas propostos. 
### Portanto, após a coleta destes dados brutos, foi feita a seleção, limpeza e formatação dos mesmos, deixando-os no formato CSV, que será nossa fonte de dados inicial do trabalho. Após isso, idealizamos a execução do projeto de arquivos com o uso de um diagrama ER facilitando a visualização dos arquivos presentes em nosso trabalho. Posteriormente, vamos utilizar arquivos binários sequenciais (estruturados) com forma de armazenamento, uma vez que haverá pouca inserção e muita consulta dos dados. Além disso, usaremos de árvore trie como índice de acesso no caso de filtragem por nome que vai auxiliar na consulta desses dados, podendo também ser feito uso de árvores B e demais algoritmo de classificação e ordenação de acordo com o dado filtrado através do índice e também tendo em vista a necessidade ao longo do desenvolvimento do trabalho.

## FUNCIONALIDADES PREVISTAS:
+ Ordenar os dados em ordem crescente (normal) ou decrescente (inversa) de acordo com os critérios Ranking de Popularidade e Título 
+ Possibilitar gerar top 10 filmes e séries (se tiver 10 elementos enquadrados no filtro) de acordo com os seguintes filtros: geral e país de origem
  
## FERRAMENTAS E BIBLIOTECAS A SEREM UTILIZADAS:
+	Jupyter (utilizado como plataforma de programação visando facilitar o acesso ao código entre os componentes da dupla além da praticidade fornecida pelo ambiente)
+ Python (será utilizada como linguagem de programação para este trabalho).
+	Github (utilizado como plataforma secundária de compartilhamento de código e somente em casos em que haja uma necessidade ou seu uso facilitaria o progresso do projeto).
+	Pandas (utilizada para organização e limpeza inicial dos dados)
+	CSV (possivelmente será utilizada pois nossa fonte de dados inicial é um arquivo do tipo CSV)
+	Biblioteca Time (Objetivando coletar dados sobre o tempo de execução dos algoritmos propostos e visando qualificar as aplicações feitas quanto ao aspecto tempo de execução).
+	Biblioteca heapq (Visando facilitar a implementação de alguns algoritmos que usam de heap como estrutura de classificação).

<h1>PROJETO DE ARQUIVOS (DIAGRAMA ER OU DIAGRAMA DE CLASSES):</h1>
  
### Como nosso conjunto de dados é proveniente dos títulos presentes na Netflix, ambos têm os mesmos atributos no dataset que utilizamos, e, portanto, nosso diagrama ER possui apenas uma entidade, sendo esta correspondente à filmes e séries da Netflix.  Os atributos desta entidade são: 
## Dicionário das variáveis:
+	imdb_id  - funciona como uma chave, sendo que cada um tem o seu imdb_id exclusivo
+	id_title - funciona como uma chave, sendo que cada um tem o seu id exclusivo
+ id_rankpop - funciona como uma chave, sendo que cada um tem o seu id exclusivo
+ id_styear - funciona como uma chave, sendo que cada um tem o seu id exclusivo
+ id_type - funciona como uma chave, sendo que cada um tem o seu id exclusivo
+ id_origincountry - funciona como uma chave, sendo que cada um tem o seu id exclusivo
+ id_language - funciona como uma chave, sendo que cada um tem o seu id exclusivo
+	title – nome do filme ou série
+	popularity - posição no ranking de popularidade da Netflix
+	startYear - ano de início
+	type - classifica como sendo filme, série, etc
+	orign_country - país de origem
+	language - idioma em que foi produzido

