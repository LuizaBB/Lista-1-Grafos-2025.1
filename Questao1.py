import pandas as pd
from ImplementacoesGrafosPython import GraphAdjMatrix as GMatrix

def printMatrix(matrix, n):
    for i in range(0, n):
        print(matrix[i])

def floydAlgorithm(graph):
    # print(graph.M)
    Dgraph=[None]*(graph.n + 1)
    Rgraph=[None]*(graph.n + 1)
    for i in range (0, graph.n+1):
        Dgraph[i]=[666]*(graph.n + 1)
        Rgraph[i]=[0]*(graph.n + 1)
    for i in range (0, graph.n+1):
        for j in range (0, graph.n+1):
            if graph.M[i][j] != 0:
                Dgraph[i][j]=graph.M[i][j]
            if graph.M[i][j] != 0:
                Rgraph[i][j]=j
    printMatrix(Dgraph, graph.n+1) #print de teste
    printMatrix(Rgraph, graph.n+1) #print de teste

if __name__== "__main__":
    input_graph=pd.read_fwf('graph1.txt', header=None)

    # print(input_graph) #print de teste
    nodesN=input_graph.iloc[0,0]
    edgesM=input_graph.iloc[0,1]
    # print(nodesN, edgesM) #print de teste
    initialNode=input_graph.iloc[1:23, 0].to_list()
    finalNode=input_graph.iloc[1:23, 1].to_list()
    costNode=input_graph.iloc[1:23, 2].astype(int).to_list()

    # print(initialNode, len(initialNode)) #print de teste
    # print(finalNode, len(finalNode)) #print de teste
    # print(costNode, len(costNode)) #print de teste

    graph=GMatrix(nodesN, directed=True)
    for i in range (0, 22):
        graph.addEdge(initialNode[i], finalNode[i], costNode[i])
    graph.print_matrix() #print de teste

    floydAlgorithm(graph)