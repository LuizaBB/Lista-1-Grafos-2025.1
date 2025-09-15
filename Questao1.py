import pandas as pd
from ImplementacoesGrafosPython import GraphAdjMatrix as GMatrix

input_graph=pd.read_fwf('graph1.txt', header=None)

print(input_graph) #print de teste
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