from typing import Generator #importação do generator (criar objetos iteraveis especificos para grafos)
from abc import ABC, abstractmethod #importação da classe e método abstratos para gerar os moldes

class GraphBase(ABC): #declaração da classe abstrata, herdando da classe abstrata base principal
  """
  Generic class for a graph
  ...
  Attributes
  ----------
  n : int
      Cardinality of the set of vertices V.
  m : int
      Cardinality of the set of edges E.
  directed : bool
      Defines if the graph is directed or not.
  """

  def __init__(self, n: int, directed: bool = False) -> None: #declaração das variáveis principais do grafo
  #método concreto (herança direta)
  #recebe o número de vértices (esperado que seja inteiro) e uma sinalização se é grafo direcionado ou não (esperado que seja bool), não retorna nada (None)
    self.n, self.m, self.directed = n, 0, directed
    #define o número de vértices como n, o número de arestas como 0 (já que ainda não foram adicionadas) e o bool de direcionamento como directed

  @abstractmethod #método abstrato: apenas para molde
  def addEdge(self, v : int, w : int): #adicionar aresta, recebe os dois vértices a serem ligados (esperado que sejam inteiros)
    ''' Adds edge vw to the graph

    Parameters
    ----------
    v : int
      first vertex.
    w : int
      second vertex.
    '''
    pass

  @abstractmethod #método abstrato: apenas para molde
  def removeEdge(self, v: int, w: int): #remove a aresta, recebe os dois vértices que compõe a aresta a ser removida
    ''' Removes edge vw from the graph
    Parameters
    ----------
    v : int
      first vertex.
    w : int
      second vertex.
    '''
    pass

  @abstractmethod #método abstrato: apenas para molde
  def getNeighbors(self, v : int, mode : str = "*", closed : bool = False) -> Generator[int, None, None]: #função para achar vizinhos, recebe o vértice, a direção de vizinhança e se tem loop
    '''Provides the neighbors of vertex v.
    Parameters
    ----------
    v : int
      vertex.
    mode : str
      Only for directed graph. "-" if input neighborhood, "+" if output neighborhood and "*" if any. tudo é em relação à v
        #+: v é a entrada, então é um aresta saindo de um outro vertice e entrando em v
        #-: v é a saída, então é um aresta saindo de v e entrando em outro vertice
        #*: Tanto saindo quanto entrando no vértice
    closed : bool
      Defines if it is a closed or open interval. True if the neighboorhood should include v or False if it should exclude.
    iterateOverNode : bool
      Defines if the iterator gives the pair of vertices (False) or a pair consisting of v and a node
    '''
    #explicação dos parametros do método feito acima
    '''
    Yields
    ----------
    int
      neighbor of vertex v.
    '''
    #retorna: generator que cria uma lista com a sequência de todos os vizinhos (útil para algoritmos que usam loops para percorrer todos os vizinhos de um vértice)
      #retoena uma lista de vertices vizinhos
    pass

  @abstractmethod #método abstrato: apenas para molde
  def isNeighbor(self, v: int, w: int) -> bool: #verifica se 2 vértices são vizinhos, recebe os dois vértices e retorna o booleano
    '''Checks if v and w are adjacent
    Parameters
    ----------
    v : int
      first vertex.
    w : int
      second vertex.
    Returns
    ----------
    bool
      True if v and w are adjacent, False otherwise.
    '''
    pass

  def V(self) -> Generator[int, None, None]: #método para gerar a sequencia iterável de vértices (herança direta ao contrário do abstrato, método concreto, por isso está definido)
    """
    Retorna a lista de vértices.
    """
    for i in range(1, self.n+1):
      yield i #adiciona no generator cada vértice dentro do loop
      #aparentemente é a listagem de todos os vértices, não em relação à um específico
        #imagino que seja útil para quando se precisa fazer sequências com arestas removidas/adicionadas, ou para gerar novos iteradores sem reclicar os antigos

  def E(self, iterateOverNode = False) -> Generator[tuple[int,int], None, None] | Generator[tuple[int, object], None, None]: #gerar lista iterável de arestas (que pode ser entre dois vértices ou um vértice e subárvore)
    """
    Retorna a lista de arestas vw
    """
    for v in self.V(): #para todo vertice na sequência de vértices iterados
      for w in self.getNeighbors(v, mode = "+" if self.directed else "*"): #para todo vértice obtido como vizinhos de um vértice da lista original
        #se for grafo direcionado, considera apenas os que tem w como entrada
        count = True #inicia definindo uma variavel de contagem como true, o que faz com que se considere de inicio reciprocidade

        if not self.directed: # avoid double counting
        #se grafo for direcionado, o for anteriormente vai ter informações duplicadas
          wint = int(w) # assures int, even if it's an object/node
          #então se separa o número do vertice que, junto com v, causa arestas duplicadas
            #int(W) separa o valor numerico do vertice ou objeto, assim se cria um criterio de consideração
          count = v < wint #nesse caso, o criterio de contagem pra escolher qual aresta vai ser considerada é se o numero da primeira for menor que o da segunda
            #se isso for true, entao count continua true (ainda se considera a aresta)
            #se for false, então count passa a ser false (nao considera a aresta em questao)
          #funciona porque é uma verificação aplicada toda vez que se seleciona um novo vizinho (e portanto se forma outra aresta)

        if count: #se count for true, é a aresta que deve ser considerada para evitar a duplicação
          yield (v,w) #adiciona o objeto iterador


class GraphAdjMatrix(GraphBase): #classe geral para controle de 1 grafo por matriz (assim como classes e objetos funcionam olha só)
  def __init__(self, n, directed = False): #declaração das variaveis iniciais do grafo
    super().__init__(n, directed) #herda a classe __init__ da classe ABC para fazer uma parte das declarações necessárias
    self.M = [None]*(self.n + 1) #cria uma lista com n+1 listas dentro (ou n+1 listas vazias)
    for i in range(0, self.n+1):
      self.M[i] = [0]*(self.n + 1) #cria-se um loop para preencher cada uma com "zeros"

  def addEdge(self, v: int, w: int, weigth: float): #metodo para adicionar aresta, recebe os vértices que vao ser ligados (esperado que sejam inteiros)
    self.M[v][w] = weigth #utiliza-os como coordenadas para, na matriz de representação, adicionar 1 (considerando como peso 1) -> funciona para direcionados
    #funciona para direcionados pois segue à risca a ordem (v,w) implicando que não necessariamente existe (w,v)
      #acredito que se fosse verdade também, teria que chamar novamente o metodo para regsitrar (w,v)
    #se fosse com peso, precisaria de outro parâmetro recebendo o peso
    #caso seja não direcionado, significa que tanto (v,w) quanto (w,v) devem ser adicionados simultaneamente
    if not self.directed: #se not false=true (no caso, confirmando que é não direcionada):
      self.M[w][v] = weigth #aplica-se a aresta no par inverso (w,v) também
    self.m += 1 #conta-se mais 1 no numero de arestas totais (já que ela não existia antes)
    #independente se for direcionada ou não (pois no não direcionada (v,w)=(w,v)=1)

  def removeEdge(self, v: int, w: int): #metodo para remover aresta, recebe os dois vertices a serem analizados (esperado que seja inteiro)
    self.M[v][w] = 0 #para tal é só colocar 0 na coordenada (v,w) dentro da matriz -> funciona apenas para direcionado
    #seguindo a lógica do método anterior, a remoção em grafos não direcionados também envolve a aresta (w,v)
    if not self.directed: #condicional que só é utilizada em não direcionado
      self.M[w][v] = 0 #coloca 0 na coordenada (w,v), pois em grafos não ordenados (v,w)=(w,v)
    self.m -= 1 #independente de ser direcionado ou não, há uma aresta sendo removida, portanto se desconta 1 do número total de arestas

  def isNeighbor(self, v, w): #método para verificar se v e w são vizinhos
    return self.M[v][w] == 1 #retorna true (se a expressão do return se mostrar verdadeira) ou false (se a expressão do return se mostrar falsa)
    #funciona tanto para n]ao direcionado (jpa que (v,w)=(w,v) quanto direcionado (já que está se avaliando uma possibilidade específica))

  def getNeighbors(self, v, mode = "*", closed = False): #método para verificar os vizinhos de um vértice v (por padrão sendo *: tanto de entrada como de saída) e considera se deve incluir ou não o próprio nó
    #imagino que seja para considerar loop no próprio vértice ou não
    #ou talvez a "ideia" de movimento vazio: Um nó é sempre vizinho dele mesmo
    #gera um objeto iterador com os vizinhos de v (importante para algoritmos)
    #aqui como se está usando um método abstrato herdado, acredito que não precise especificar a saída da função (apenas parâmetros para garantir continuidade)
    if closed: #se a condição de "própria vizinhança" for atendida
      yield v #adiciona o próprio ve´rtice na lista do objeto

    w = 1 #variável auxiliar para percorrer todos os vértices presentes no grafo (variável de contagem)

    while w <= self.n: #enquanto a variável auxiliar não chega ao total de vértices
      if self.directed: #se o grafo for direcionado (onde (v,w) != (w,v))
        if mode == "*" and (self.isNeighbor(v, w) or self.isNeighbor(w, v)): #se for para procurar tanto por entrada quanto por saída, além de que existe aresta em (v,w) e (w,v)
          #como esse pede tanto saída quanto entrada, ambos (v,w) e (w,v) tem que existir
            yield w #caso sim, adiciona o vértice analisado
            #como está se verificando apenas 1 vértice v para vizinhos, ele se mantém fixo enquanto o outro lado do par (w) varia
        elif mode == "+" and self.isNeighbor(v, w): #se for apenas de entrada (v é entrada e w saída), a aresta verificada é com v à direita (v,w) pois o sentido de leitura da aresta é v<-w
            yield w #se afirmativo, então adiciona o outro vértice no objeto
        elif mode == "-" and self.isNeighbor(w, v): #se for apenas de saída (v é saída e w entrada), a aresta verificada é com v à esquerda, pois a ordem de leitura seria w<-v
            yield w #caso sim, adiciona o vértice estudado no objeto iterador
      else: #se for não direcionado, nenhum dos modos importa
        if self.isNeighbor(v, w): #basta a verificação de apenas uma das possibilidades. Caso seja satisfeita
          yield w #adiciona o contador (que representa outro vértice) ao objeto iterador

      w += 1 #adiciona 1 na variável temporária para garantir que sejam checadas os outros vértices (não entre num loop e cague o objeto todo)
#OBS importante: No estudo de grafos as matrizes de adjacencias são contadas de 1 para frente (geralmete não se utiliza zero para um vértice), portanto a matriz criada tem n+1 índices para que o índice 0 não seja usado (por isso w=1)
  def printMatrix(self, k): #método criado para impressão de matriz, considerando a existencia de vértice 0 ou não
    for i in range(k, self.n+k):
      print(self.M[i][k: self.n+k])