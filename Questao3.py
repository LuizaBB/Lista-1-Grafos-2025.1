'''
Comentários para entendimento do problema:
Entrada: mapa com:
    Celulas de caminho livre, com custo 1
    Obstáculos intransporivel (custo muito elevado) - sem existencia de aresta
    Piso diíficl com custo 3
    S: início
    G: Fim
    Pode-se movimentação pelos 4 lados (nNorte, Sul, Leste e Oeste)
Com isso:
    Entrada é um mapa com arestas de peso diferentes, mas que provavelmente não são negativas
        Caminhos inexistentes podem ser representados tanto por arestas muito altas quanto negativas
        Isso dá brecha para usar Bellmann ou Dijsktra
        No caso de considerar 
    Não entendi a função dos pontos
        O ponto vai ser interpretado como substituição ao =, já que a documentação só fala de = mas não tem = no exemplo
'''
import pandas as pd
from ImplementacoesGrafosPython import GraphAdjMatrix as GMatrix
from ImplementacoesGrafosPython import GraphAdjList as GList

def analiseNeighboors(Input, node):
    neighboorList=[(i, j+1), (i, j-1), (i+1, j), (i-1, j)] #leste, oeste, norte, sul
    for neigboor in neighboorList:
        match Input[neigboor[0], neigboor[1]]:
            case "":

    return neighboorList

if __name__== "__main__":

    Input=[]
    with open("grid_example.txt", 'r') as input:
        for line in input:
            final_Line=line.strip("\n")
            Input.append(final_Line)
    print(Input) #print de teste
    print(Input[0].split(" ")[0]) #print de teste
    rowsMap=int(Input[0].split(" ")[0])
    collumnsMap=int(Input[0].split(" ")[1])
    print(rowsMap, collumnsMap) #print de teste

    obstaclesNodes=0
    graphEdges={}
    for i in range(1, rowsMap):
        currentRow=Input[i]
        for j in range(0, collumnsMap):
            # print(currentRow[j]) #print de teste #animação fofa
            if currentRow[j]=='#':
                obstaclesNodes+=1
            else:
                # edgeValue=0
                # beginNode=(0, 0)
                # endNode=(0, 0)
                # match currentRow[j]:
                #     case "S":
                #         beginNode=(i, j)
                #     case "G":
                #         endNode=(i, j)
                #     case ".":
                #         edgeValue=1
                #     case "~":
                #         edgeValue=1
                neighboorList=analiseNeighboors(Input, (i, j))
                for edge in neighboorList:
                    if edge!='#':
                        edgeElement={(j, i): edgeValue}
                        graphEdges.update(edgeElement)
    totalNodes= (rowsMap*collumnsMap)-obstaclesNodes #quantidade total de nós desconsiderando os obstáculos
    print(graphEdges) #print de testes
    print(obstaclesNodes, totalNodes) #print de teste
        

    # inputMap=pd.DataFrame(Input, index=None, columns=None)
    # # '''
    # print(inputMap)
    # print(inputMap.iloc[0,0])
    # print(inputMap.iloc[0,0][0])
    # print(inputMap.iloc[0,0][1])
    # # '''
    # rows=int(inputMap.iloc[0,0][0]+inputMap.iloc[0,0][1])
    # collumns=int(inputMap.iloc[0,0][3]+inputMap.iloc[0,0][4])
    # print(rows, collumns, type(rows)) #print de teste

    