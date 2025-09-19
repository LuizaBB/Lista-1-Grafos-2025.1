import pandas as pd
from ImplementacoesGrafosPython import GraphAdjMatrix as GMatrix

def printMatrix(matrix, k):
    n=len(matrix[0])-1 #considerando matriz quadrada, considerando grafo com tamanho (0, N+1)
    for i in range(k, n+k):
        print(matrix[i][k: n+k])

def sumRow(row):
    result=0
    for i in range(0, len(row)):
        result+=row[i]
    return result

def floydAlgorithm(graph, intervalRef):
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
    # print("print matriz declarada")
    # printMatrix(D, intervalRef) #print de teste
    # printMatrix(R, intervalRef) #print de teste

    for k in range(intervalRef, n+intervalRef):
        for i in range(intervalRef, n+intervalRef):
            for j in range(intervalRef, n+intervalRef):
                if D[i][k]+D[k][j]<D[i][j]:
                    D[i][j]=D[i][k]+D[k][j]
                    R[i][j]=R[i][k]
    # print("print matriz final")
    # printMatrix(D, intervalRef) #print de teste
    # printMatrix(R, intervalRef) #print de teste
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
    k=min(min(initialNode), min(finalNode)) #primeiro nó (considerando que os vértices seguem uma ordem crescente) #referência de vértice e intervalo

    # print(initialNode, len(initialNode)) #print de teste
    # print(finalNode, len(finalNode)) #print de teste
    # print(costNode, len(costNode)) #print de teste
    # print(k) #print de teste

    graph=GMatrix(nodesN)
    for i in range (0, edgesM):
        graph.addEdge(initialNode[i], finalNode[i], costNode[i])
    # print("print matriz lida")
    # graph.printMatrix() #print de teste

    
    D, R = floydAlgorithm(graph, k)

    nodeSum=[]
    for i in range(k, nodesN+k):
        nodeSum.append(sumRow(D[i]))
    # print("Lista de soma das distancias para cada vértice")
    #print(nodeSum) #print de teste

    centralNode=nodeSum.index(min(nodeSum))+k #nó central
    # print(centralNode) #print de teste
    centralNode_distanceList=D[centralNode][k: nodesN+k] #vetor de distâncias em relação ao central
    # print(centralNode_distanceList) #print de teste
    mostDistantNode=centralNode_distanceList.index(max(centralNode_distanceList))+k #vértice mais longe do central
    # print(mostDistantNode) #print de teste
    
    #respostas:
    print(f"Pela matriz dada:\n   Nó escolhido como central: {centralNode}\n   Distâncias em relação ao nó central: {centralNode_distanceList}\n   Vértice mais distante do central: {mostDistantNode}\n   Matriz de backtracking: ")
    printMatrix(R, k)