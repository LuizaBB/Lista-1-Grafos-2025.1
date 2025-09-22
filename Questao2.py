import pandas as pd
from ImplementacoesGrafosPython import GraphAdjMatrix as GMatrix

def Bellmann_FordAlgorithm(graph, nodeReference):
    n=graph.n
    D=[]
    anterior=[]
    for i in range(0, n):
        anterior.append(0)
        if i==nodeReference:
            D.append(0)
        else:
            D.append(100)
    Edges={}
    for j in range(0, n):
        for i in range(0, n):
            if graph.M[j][i] != 0:
                edgeElement={(j, i): graph.M[j][i]}
                Edges.update(edgeElement)
    for edge in Edges:
        j, i=edge
        if D[i] > D[j] + Edges[edge]:
            D[i] = D[j] + Edges[edge]
            anterior[i]=j
    return D, anterior
    
if __name__== "__main__":

    Input=[]
    with open("graph2.txt", 'r') as input:
        for line in input:
            final_Line=line.strip("\n").split("\t")
            Input.append(final_Line)
    inputGraph=pd.DataFrame(Input)

    nodesN=int(inputGraph.iloc[0,0])
    edgesM=int(inputGraph.iloc[0,1])
    initialNode=inputGraph.iloc[1:edgesM+1, 0].astype(int).to_list()
    finalNode=inputGraph.iloc[1:edgesM+1, 1].astype(int).to_list()
    costNode=inputGraph.iloc[1:edgesM+1, 2].astype(int).to_list()

    graph=GMatrix(nodesN, directed=True)
    for i in range (0, edgesM):
        graph.addEdge(initialNode[i], finalNode[i], costNode[i])
    k=0     #considerando o vértice de referencia = 0

    D, anterior = Bellmann_FordAlgorithm(graph, k)

    ShortWay06=[6]
    i=6
    while True:   
        ShortWay06.append(anterior[i])
        if anterior[i]==0: 
            break
        i=anterior[i]
    stringShortWay06=""
    for i in range(len(ShortWay06), 0, -1):
        stringShortWay06+=str(ShortWay06[i-1])
        if i!=1:
            stringShortWay06+="->"

    #respostas
    print("Baseado na matriz dada:")
    print(f"    Custo do caminho mínimo do vértice 0 a 6: {D[6]}")
    print(f"    Caminho mínimo realizado do vértice 0 até 6: {stringShortWay06}")


