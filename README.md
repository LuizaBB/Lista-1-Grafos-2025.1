# Lista 1 Grafos 2025.1
 Lista de Algoritmos para Caminho Mínimo
>Os algoritmos implementados foram baseados nos pseudocódigos contidos no livro **Grafos: Introdução e Prática** (Boaventura Netto, Paulo Oswaldo)
## Instruções de compilação:

## Questão 1: Estação central para metrô
Considerando que a questão oferta um grafo **não direcionado** represetando as estações de um metrô e precisa, como primeiro passo, definir a estação central para o mesmo, foi escolhido o algoritmo de caminho mínimo FLoyd, por trabalhar com o cálculo de distâncias mínimas com relação à todos os vértices (não somente em relação à um vértice de referência, como Bellmann-Ford e Dijkstra), o que fornece uma base de informações mais ampla para encontrar o vértice central (definido como aquele que tem menor custo possível para os outros vértices).
### Em relação à implementação
Considerando que o algoritmo Floyd se baseia apenas em matrizes, o ínicio da implementação envolveu aplicar a representação de matrizes adjacentes para o grafo de entrada com a linha 54 para criação do objeto Grafo e linhas 55 a 56 para preenchimento do grafo de acordo com a entrada dada.  
Além disso, a função contendo o algoritmo recebe dois parâmetros: O grafo em si e o "primeiro vértice" do mesmo denominada "IR" (considerando que os vértices seguem uma ordem crescente), visando ajustar o tamanho das matrizes e dos intervalos ao longo da implementação (principalmente para processar tanto matrizes com vértices [0, 1, 2, ...] quanto [1, 2, 3, ...]).  

O pseudocódigo inicia com a declaração de duas matrizes tamanho N X N com ``D=[None]*(n + 1)`` e ``R=[None]*(n + 1)``[1] D (recebe a matriz que representa o grafo) e R (das coordenadas (i,j) que representam uma aresta, recebe o segundo vértice j). A delimitaçaõ da quantidade de linhas N para ambas matrizes ocorre nas linhas 17 e 18, as quais declaram D e R com ma quantidade N+1 de listas vazias, respectivamente (N+1 para o caso do grafo utilizar um intervalo de vértices [1, N+1], e vazia porque será preenchida com outras listas para as colunas). Na aplicação do algoritmo ambas foram preenchidas simultaneamente (possível por ambas terem o mesmo tamanho) com um *for loop* com *range* (0, N+1) em ``for i in range (0, n+1):``[1], que preenche a matriz D com 1000 (o inteiro máximo escolhido para representar arestas inexistentes) na linha ``D[i]=[1000]*(n + 1)``[1] e R com 0 (inteiro usado para indicar impossibilidade de backtracking, pela falta de aresta) na linha ``R[i]=[0]*(n + 1)``[1], que correspondem às linhas 19 à 21.

Nas linhas 22 à 28 tem o tratamento inicial dessas matrizes antes do algoritmo em si: Com dois *for loops* com intervalo (IR, N+IR) pelas linhas ```for i in range (IR, n+IR): for j in range (IR, n+IR):```[1] verifica se a coordenada (i,j) no grafo é diferente de 0(``if graph.M[i][j] != 0``) (se sim, há aresta para ser colocada na matriz D e vértice *j* na matriz R) e se *i=j* (``if i==j:``) (em caso afirmativo, se trata de um laço (entra e sai do próprio vértice) e, não se considerando a possibilidade deles, na matriz D será marcado como 0, já que não é necessário nenhum movimento para se chegar aonde já está)[1].

Entre a linha 29 a 35 há o processamento feito pelo algoritmo em si: Inicia com a linha de código ``for k in range(IR, n+IR):``[2] que cria um look com tamanho das matrizes D e R para a variável *k* que representa o vértice de referência atual no algoritmo (à cada novo ciclo *k* representará cada vértice do grafo como referência). Dentro deste *loop* ainda se tem outros dois *loops* ``for i in range(IR, n+IR):``[3] e ``for j in range(IR, n+IR):``[3] de tamanho (IR, N+IR) com as variáveis *i* e *j* para (representando os vértices no formato de aresta *(i, j)*). Com eles é possível no grafo com base nos vértices e , quando a condição ``if D[i][k]+D[k][j]<D[i][j]:``[4] (Se a distância considerando *k* como vértice intermediário for menor que a distância atual de *i* para *j*) é atendida, a distância *(i, j)* na matriz D e o *backtracing* na R são atualizados com ``D[i][j]=D[i][k]+D[k][j]``[5] e ``R[i][j]=R[i][k]``[6], respectivamente. Após o *loop* principal ser encerrado (a análise de minimização ser feita considerando todas os vértices como referência) retorna a matriz D com as distâncias mínimas e matriz R com o caminho recursivo atualizadas.
>As linhas do pseudocódigos relacionadas:

>[1]: inicio <dados G = (V,E); matriz de valores V(G); matriz de roteamento R=[rij]; rij=j ; D=[dij]=V(G)

>[2]: para k=1, ..., n fazer[ k é o vértice-base da iteração ]

>[3]: para todo i, j= 1,.., n fazer

>[4]: se dik + dkj < dij

>[5]: dij = dik + dkj

>[6]: rij = rik

## Questão 1: Otimizando caminhos por regeneração
Considerando que a questão fornece um grafo **direcionado** contendo arestas positivas e negativas e requer um caminho mínimo sempre envolvendo os mesmos vértices (de 0 para 6), foi escolhido o algoritmo Bellmann-Ford para a resolução, visto que este algoritmo retorna vetores de distâncias mínimas e *backtracking* sempre em referência à um único vértice (característica que algoritmos como Floyd não possuem) e suporta arestas positivas e negativas (característica que algortimos como Djikstra não possuem).
### Em relação à implementação
A implimentação foi iniciada na linha 5 com a obtenção da quantidade de vértices existentes no grafo através o objeto criado para o mesmo (``n=graph.n``)[1], importante para a declaração futura dos vetores-resposta. Em seguida a declaração das variáveis (em formato de lista) que serão os resultados finais em ``D=[]``[1] e ``anterior=[]``[1] (que receberão as distâncias mínimas e *backtracking*, respectivamente) nas linhas 6 e 7 e o preenchimento dessas listas de acordo com os requerimentos do pseudocódigo (na lista D inteiro máximo para todos os índices exceto o de referência [1] com ``if i==nodeReference: D.append(0)``[1] e ``else: D.append(100)``[1], além do "anterior" totalmente preenchido por zeros [1] com ``anterior.append(0)``[1]) nas linhas 8 a 13. 

Nas linhas 14 a 19 tem-se a formação da relação das arestas e seus pesos: Representada em dicionário la linguagem Python pois permite uma obtenção direta do custo de cada aresta por um sistema chave-valor (que facilita a varredura futura aplicada no algoritmo), declarada inicialmente vazia com ``Edges={}``[2], aos poucos completada por dois *loops* ``for j in range(0, n):``[2] e ``for i in range(0, n):``[2] que percorrem a matriz de adjacência verificando as arestas que não são definidas com 0 (``if graph.M[j][i] != 0:`` [2]) para identificar arestas existentes e, em caso positivo adicioná-las no dicionário com o formato {(vértice1, vértice2) : custo} com as linhas ``edgeElement={(j, i): graph.M[j][i]}``[2] e ``Edges.update(edgeElement)``[2]. Ao final deste processo o dicionário de arestas está pronto para ser utilizado na aplicação efetiva do algoritmo (este processo foi também implementado como um método dentro de GMatrix no arquivo "ImplementacoesGrafosPython", mas não utilizado por ser requerimento para uma tarefa muito específica, não sendo utilizada o suficiente para se tornar método).

Na aplicação em si, concentrada nas linhas 20 à 25, é declarado um *loop* na linha ``for edge in Edges:``[2] para percorrer toda a relação de arestas, em seguida separar os vértices que a compõe com ``j, i=edge``[2] e aplicar na condição ``if D[i] > D[j] + Edges[edge]:``[2] que avalia se a adição da aresta analisa diminui o custo de "vértice1" à "vértice2" (como está tudo em relação à um único vértice, o svalores obtidos no vetor D avaliam de a distância do vértice1 até o vértice de referência diminui caso adicionado um caminho intermediário (vértice1, vértice2)). Em caso positivo, o vetor de distâncias tem seu valor mudado considerando essa nova distância mínima com ``D[i] = D[j] + Edges[edge]``[3], além da mudança no vetor "anterior" adicionando um novo *backtracking* com ``anterior[i]=j``[4].

Com esse processo aplicado à todas as arestas, os vetores D e "anterior" declarados inicialmente são atualizados com todos os caminhos mínimos e "rotas" de volta em relação ao vértice escolhido (que, no caso da questão, sempre será 0) que são retornados na linha ``return D, anterior``, o que permite calcular a distância mínima e seu processo até qualquer vértice do grafo (no caso da questão, especificado como 6).
>As linhas do pseudocódigos relacionadas:

>[1]: d11 <-0; di1<- ∞ ∀ i ∈ V-{1}; anterior(i) <- 0 ∀ i

>[2]: enquanto ∃ (j, i) ∈ A | d1i > d1j +vij fazer

>[3]: d1i = d1j +vij

>[4]:  anterior(i) <- j