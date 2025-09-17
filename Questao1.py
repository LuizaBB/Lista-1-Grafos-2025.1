import pandas as pd
from ImplementacoesGrafosPython import GraphAdjMatrix as GMatrix

def printMatrix(matrix, n):
    for i in range(0, n):
        print(matrix[i])

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
    print("print matriz declarada")
    printMatrix(D, n+1) #print de teste
    printMatrix(R, n+1) #print de teste
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if D[i][k]+D[k][j]<D[i][j]:
                    D[i][j]=D[i][k]+D[k][j]
                    R[i][j]=R[i][k]
    print("print matriz final")
    printMatrix(D, n+1) #print de teste
    printMatrix(R, n+1) #print de teste
    return D, R

if __name__== "__main__":
    input_graph=pd.read_fwf('graph1.txt', header=None)

    # print(input_graph) #print de teste
    nodesN=input_graph.iloc[0,0]
    edgesM=input_graph.iloc[0,1]
    # print(nodesN, edgesM) #print de teste
    initialNode=input_graph.iloc[1:edgesM+1, 0].to_list()
    finalNode=input_graph.iloc[1:edgesM+1, 1].to_list()
    costNode=input_graph.iloc[1:edgesM+1, 2].astype(int).to_list()

    # print(initialNode, len(initialNode)) #print de teste
    # print(finalNode, len(finalNode)) #print de teste
    # print(costNode, len(costNode)) #print de teste

    graph=GMatrix(nodesN, directed=True)
    for i in range (0, edgesM):
        graph.addEdge(initialNode[i], finalNode[i], costNode[i])
    print("print matriz lida")
    graph.print_matrix() #print de teste

    D, R = floydAlgorithm(graph)

    nodeSum=[]
    for i in range(1, graph.n+1):
        nodeSum.append(sumRow(D[i]))
    print(nodeSum) #print de teste

    centralNode=nodeSum.index(min(nodeSum))+1 #nó central
    print(centralNode) #print de teste
    centralNode_distanceList=D[centralNode][1: nodesN] #vetor de distâncias em relação ao central
    print(centralNode_distanceList) #print de teste
    mostDistantNode=centralNode_distanceList.index(max(centralNode_distanceList))+2 #vértice mais longe do central
    print(mostDistantNode) #print de teste