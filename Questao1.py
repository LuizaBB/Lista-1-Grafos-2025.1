import pandas as pd
from ImplementacoesGrafosPython import GraphAdjMatrix as GMatrix

input_graph=pd.read_fwf('graph1.txt')
print(input_graph) #print de teste
nodesN=input_graph.iloc[0,0]
edgesM=input_graph.iloc[0,1]
print(nodesN, edgesM) #print de teste
initialNode=input_graph.iloc[1:22, 0]
finalNode=input_graph.iloc[1:22, 1]
costNode=input_graph.iloc[1:22, 2]
print(initialNode)
print(finalNode)
print(costNode)
# print(input_graph.iloc[1:22, 0])
# graph=GMatrix()