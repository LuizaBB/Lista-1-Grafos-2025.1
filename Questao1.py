import pandas as pd
from ImplementacoesGrafosPython import GraphAdjMatrix as GMatrix

def printMatrix(matrix):
    n=len(matrix[0]) #considerando matriz quadrada
    for i in range(1, n):
        print(matrix[i][1: n])

def sumRow(row):
    result=0
    for i in range(0, len(row)):
        result+=row[i]
    return result

def floydAlgorithm(graph):
    n=graph.n
    D=[None]*(n + 1)
    R=[None]*(n + 1)
    for i in range (0, n+1):
        D[i]=[1000]*(n + 1)
        R[i]=[0]*(n + 1)
    for i in range (1, n+1):
        for j in range (1, n+1):
            if graph.M[i][j] != 0:
                D[i][j]=graph.M[i][j]
            elif i==j:
                D[i][j]=0
            if graph.M[i][j] != 0:
                R[i][j]=j
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if D[i][k]+D[k][j]<D[i][j]:
                    D[i][j]=D[i][k]+D[k][j]
                    R[i][j]=R[i][k]
    return D, R

if __name__== "__main__":
    input_graph=pd.read_fwf('graph1.txt', header=None)

    nodesN=input_graph.iloc[0,0]
    edgesM=input_graph.iloc[0,1]
    initialNode=input_graph.iloc[1:edgesM+1, 0].to_list()
    finalNode=input_graph.iloc[1:edgesM+1, 1].to_list()
    costNode=input_graph.iloc[1:edgesM+1, 2].astype(int).to_list()


    graph=GMatrix(nodesN, directed=True)
    for i in range (0, edgesM):
        graph.addEdge(initialNode[i], finalNode[i], costNode[i])

    D, R = floydAlgorithm(graph)

    nodeSum=[]
    for i in range(1, graph.n+1):
        nodeSum.append(sumRow(D[i]))

    centralNode=nodeSum.index(min(nodeSum))+1 #nó central
    centralNode_distanceList=D[centralNode][1: nodesN] #vetor de distâncias em relação ao central
    mostDistantNode=centralNode_distanceList.index(max(centralNode_distanceList))+2 #vértice mais longe do central
    
    #respostas:
    print(f"Pela matriz dada:\n   Nó escolhido como central: {centralNode}\n   Distâncias em relação ao nó central: {centralNode_distanceList}\n   Vértice mais distante do central: {mostDistantNode}\n   Matriz de backtracking: ")
    printMatrix(R)