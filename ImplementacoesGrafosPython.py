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

  def getEdges(self):
    edges={}
    for j in range(0, self.n):
        for i in range(0, self.n):
            if self.M[j][i] != 0:
                edgeElement={(j, i): self.M[j][i]}
                edges.update(edgeElement)
    return edges
  
class GraphAdjList(GraphBase): #aqui a classe geral que vai representar o grafo em formato de lista
#como é uma lista, o grafo tem 2 partes principais: as listas e os nós que compõe as listas
  #como é python, a aplicação simplifica a parte de arrays e listas para apenas listas: téra uma lista princilap para os vértices e listas menores para os vizinhos
#por causa dessa lógica é necessário formar ainda 2 classes dentro da classe do grafo: um para os nós (pois gerarão os objetos nós, que cada um carregará um vértice) e a classe lista (que vai gerar os objetos listas, visto que cada lista terá um papel diferente)
#com uma classe principal e 2 subclasses se garante que as listas e nós alterados sejam pertencentes ao mesmo grafo.
  class Node(object): #classe responsável pela criação e edição de objetos nós
  #node é vértice em ingles, então o nome segue a mesma linha da classe Edge
    """ Definition of node
    ...

    Attributes
    ----------
    value : int
        Value of node
    edge : Edge
        Edge which the node represents.
    next : Node
        "Pointer" to next node

    """
    def __init__(self) -> None: #iniciação e declaração: à princípio está vazio pois quem vai preenchê-lo será a lista
      self.value = None #declara o valor do vértice (próprio caso seja a lista principal ou vizinho se for a alista auxiliar)
      self.edge = None #declara a aresta que representa
      self.next = None #declara o "ponteiro" para o próximo nó, criando a ideia de lista

    def __int__(self) -> int: # para facilitar a comparação e exibição 3método para retornar os valores contidos no nó
      return self.value

  class Edge(object): #classe de listas (chamada de Edges provavlmente porque são as arestas que fazem a conexão entre os vértices (?)) não concordo muito mas tudo bem
    def __init__(self): #declaração (à princípio a lista está vazia)
      self.v1, self.node1 = None, None #declara o vértice 1 (e seu respectivo nó)
      self.v2, self.node2 = None, None #declara o vértice 2 (e seu respectivo nó)
      #declarando os dois elementos da arestas, é possível fazer a ligação entre eles e, portanto, a lista (?)
      #OBS:Como está dentro de um __init__ (assim como todos objetos de POO), chamar Edge() no código principal apenas faz o "alocamento de memória", mas não cria nem delacara essas variáveis automaticamente
        #esse método sera utilizado por outros métodos ao longo da classe como apoio e organização

  def __init__(self, n, directed = False, doublyLinkedList = False, iterateOverNode = False): #continuação da declaração
    super().__init__(n, directed) #herda as definições do __init__ anterior (para não ser repetitivo)
    self.L = [None]*(self.n + 1) #declara uma lista com o tamanho de vértices (a lista principal)
      #puxa a ideia de índice especificada na matriz de adjacência
    for i in range(1, self.n + 1): #para cada índice da lista principal
      self.L[i] = GraphAdjList.Node() # head nodes #cria-se a lista auxiliar para os vizinhos de cada nó
      #como se considera que os vértices do grafo são números consecutivos começando do 1, os índices é uma referência para mapear as listas

    self.doublyLinkedList = doublyLinkedList #adiciona booleano se é não direcionado (lista duplamente encadeada) ou não (simplismente encadeada)
      #imagino que, se for duplamente encadeada, utiliza esse booleano para estabelecer o "duplo" caminho
    self.iterateOverNode = iterateOverNode # adiciona booleano de incluir ou não o próprio vértice em outras funções (como obter os vizinhos)


  def addEdge(self, v, w): # método de adicionar arestas, recebendo os dois vértices que compõe a aresta
  #o objetivo principal é adicionar aresta (addEdge), mas que precisa de outro método mais específico para funcionar (addToList)
    def addToList(v, w, e, mode): #um submétodo que faz a adição do vértice na lista auxiliar, formando a aresta
      node = GraphAdjList.Node() #cria-se um novo objeto nó para armazenar o vértice vizinho
        #por isso que a classe do nó somente possui declaração e visualização, as manipulações principais são da lista

      node.value = w #esse novo nó possui o vértice vizinho w
      node.edge = e #cria a variável de aresta do nó e define como a aresta passada
      node.next = self.L[v].next #o nó criado é ligado à lista auxiliar do vértice principal específico
        #ligado no sentido: o nó criado recebe como próximo endereço a cabeça atual da lista auxiliar
        #isso não garante uma ligação direta (pois não se tem acesso ao novo nó através da lista)
      self.L[v].next = node #conclui a ligação estabelendo o caminho lista principal->lista auxiliar
        #ligado no sentido: na lista principal (de vizinhos) desse vértice recebe o nó criado
          #logo o nó criado vira a próxima cabeça dessa lista auxiliar específica
    #OBS: Essa parte só estabelece corretamente o sentido lista principal -> lista auxiliar, visto que é o processo de se inserir uma cabeça nova sem perder o resto do corpo

      if self.doublyLinkedList: #se for aplicar com o conceito de lista duplamente encadeada (eu acho)
      #agora não sei exatamente porque precisaria de lista duplamente encadeada em grafos
        self.L[v].next.prev = self.L[v] #cria-se uma nova variável no nó para armazenar um anterior ao mesmo, que agora
        #self.L[i] é um índice da lista principal, .next é a parte desse nó que guarda o "endereço" do proximo nó (sendo que self.L[i].next já existe)
          #logo self.L[i].next.previous é uma variável nova dentro de um nó, que representa (em relaçao à um nó que se está atualmente) o nó anterior que o p´roximo nó está ligado
            #ou seja, o próprio nó que se está atualmente porém com outras palavras, ou melhor, seguindo outro caminho:
              #nó atual -> pula para próximo nó -> do próximo nó acessa a variável de nó anterior
        #portanto essa linha faz especificamente essa ligação: agora confirma-se que o nó à frente está diretamente ligado com o nó atrás (permitindo a dupla ligação direta)
          #que concretiza a ligação dupla: antes já havia a ligação
    #OBS: Com este processo aqui que se estabelece o sentido lista auxiliar -> lista principal, principalmente pela variável prev (previous) que guarda o endereço do nó anterior a elw
      #ao contrário de antes (que só tinha endereço para se mover para frente) tem endereço para se mover para frente e para trás

        if self.L[v].next.next != None: #se o endereço que guarda o segundo nó não estiver vazio (portanto após a cabeça ainda há mais lista)
        #considernaod que self.L[v].next agora é a nova cabeça, self.L[v].next.next seria o segundo nó da lista auxiliar após a adição da nova cabeça (e portanto é a antiga cabeça)
        #ainda está dentro da condição de ser duplamente encadeado, então acho que é para aplicar isso nesse próximo nó
          self.L[v].next.next.prev = self.L[v].next #logo esse segundo nó (a parte que guarda o nó anterior) vai efetivamente realizar o duplo encadeamento
          #self.L[i].next.next é o segundo nó da lista auxiliar de um vértice v e self.L[i].next é primeiro nó (cabeça)

      if self.directed: #se o grafo for direcionado, a adição na lista também precisa indicar a "direção" da vizinhança
      #se for não direcionado essa etapa de sentido não é necessária
        node.mode = mode #cria-se uma variável com o sentindo da aresta e adicona no nó

      return node #aqui acaba o método de adicionar nó à lista na cabeça (técnica específica para adicionar o vizinho, no contexto mais geral do grafo)
      #esse método é importante porque vai ser chamado posteriormente (dentro do método addEdge) para adicionar finalmente as viiznhanças
      #tipo o código so SystemVerilog: não necessariamente segue a sequencia lógica das ideias escritas

    #continuação do método geral para adicionar a aresta (que recebe) o nó cabeça da lista auxiliar devidamente ligado.
      #como recebe apenas o nó, tem duas possibilidades
        #grafo direcionado: o novo nó (nova cabeça) só tem o endereço que "aprofunda" na lista auxiliar, sem conseguir voltar para a lista principal
        #grafo nao direcionado: a nova cabeça tem uma variável que permite "voltar" para a lista principal, então pode-se percorrer duplamente
      #aqui que começa o início do processo (formar as arestas) para terminar em addToList (implementando as arestas nas listas)

    e = GraphAdjList.Edge() #aqui se cria a aresta desejada com o __init__do inicio da classe
      #mais especificamente a declaração das variáveis necessárias no processo de criação da aresta
    e.v1, e.v2 = v, w #atribui os vértices em seus respectivos lugares na aresta (para formar o par)

    e.node1 = addToList(v, w, e, "+") #chama o método addToList para adiconar w na lista de v (considerando v como entrada e w saída)
    e.node2 = addToList(w, v, e, "-") #chama addToList para adicionar v na lista de w (considerando v como saída e w como entrada)
    #essa logica de linhas é aplicado tanto para grafos direcionados quanto não direcionados:
      #grafos não direcionados: a variável mode não é criada em cada nó, portanto a ação feita é apenas colocar um vértice na lista auxiliar do outro
      #grafos direcionados:
        #a primeira linha considera o par (v,w), portanto declara v como entrada e w como saída, no esquema v->w
        #a srgunda linha considera o par (w,v), portanto considera w como saída e v como entrada, no esquema w->
        #assim é colocada a mesma informação (em interpretações diferentes) em listas diferentes, garantindo que a relação direcionada pode ser indentificada em qualquer um dos vértices

    self.m += 1 #aumenta a contagem geral de arestas em 1

  def removeEdge(self, e): #método para a remoção de uma aresta
  #nao consegui entender como eu passo a aresta como parametro na função principal (tirar essa duvida proxima semana)
  #para a remoção de arestas (atividade específica), uma etapa necessária é a remoção de nós de uma lista (atividade geral)
    def removeFromList(node): #método para remover nós das listas
      node.prev.next = node.next #
      #node é o nó que o método recebe quando é chamado (futuramente dentro de removeEdge)
      #nde.prev é o nó anterior ao passado (dentro da lista auxiliar)
      if node.next != None:
        node.next.prev = node.prev
    removeFromList(e.node1)
    removeFromList(e.node2)

    self.m -= 1 #decresce 1 na contagem geral de arestas (independente se for direcionado ou não)

  def getNeighbors(self, v: int, mode: str = "*", closed: bool = False): #metodo para criar um objeto iterador que seleciona os vizinhos
    if closed:
      node = GraphAdjList.Node()
      node.value = v

      yield node if self.iterateOverNode else v

    node = self.L[v].next

    while node != None:
      if self.directed:
        if mode == "*" or node.mode == mode:
          yield node if self.iterateOverNode else node.value
      else:
        yield node if self.iterateOverNode else node.value

      node = node.next


  def isNeighbor(self, v, w):
    mode = "+" if self.directed else "*"

    for node in self.getNeighbors(v, mode):
      if node.value == w:
        return True

    return False
