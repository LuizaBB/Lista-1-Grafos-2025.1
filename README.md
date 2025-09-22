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
