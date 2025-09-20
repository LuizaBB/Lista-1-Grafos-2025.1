import pandas as pd
from ImplementacoesGrafosPython import GraphAdjMatrix as GMatrix

if __name__== "__main__":

    Input=[]
    with open("graph2.txt", 'r') as input:
        for line in input:
            final_Line=line.strip("\n").split("\t")
            Input.append(final_Line)
    inputGraph=pd.DataFrame(Input)
    print(inputGraph) #print de teste

    nodesN=int(inputGraph.iloc[0,0])
    edgesM=int(inputGraph.iloc[0,1])
    print(f"N° de nós e vértices: {nodesN}, {edgesM}") #print de teste
    initialNode=inputGraph.iloc[1:edgesM+1, 0].astype(int).to_list()
    finalNode=inputGraph.iloc[1:edgesM+1, 1].astype(int).to_list()
    costNode=inputGraph.iloc[1:edgesM+1, 2].astype(int).to_list()

    print(initialNode, len(initialNode)) #print de teste
    print(finalNode, len(finalNode)) #print de teste
    print(costNode, len(costNode)) #print de teste

    graph=GMatrix(nodesN, directed=True)
    for i in range (0, edgesM):
        graph.addEdge(initialNode[i], finalNode[i], costNode[i])
    k=0 #considerando o vértice de referencia = 0
    print("Grafo lido")
    graph.printMatrix(k) #print de teste 

