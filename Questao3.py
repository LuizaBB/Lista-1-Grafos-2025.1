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

def printMatrix(matrix, k):
    n=len(matrix[0])-1 #considerando matriz quadrada, considerando grafo com tamanho (0, N+1)
    for i in range(k, n+k):
        print(matrix[i][k: n+k])

if __name__== "__main__":

    Input=[]
    with open("grid_example.txt", 'r') as input:
        for line in input:
            final_Line=line.strip("\n")
            Input.append(final_Line)
    inputMap=pd.DataFrame(Input)
    print(inputMap)
    print(inputMap.iloc[0,0])
    print(inputMap.iloc[0,0][0])
    print(inputMap.iloc[0,0][1])
    rows=int(inputMap.iloc[0,0][0]+inputMap.iloc[0,0][1])
    collumns=int(inputMap.iloc[0,0][3]+inputMap.iloc[0,0][4])
    print(rows, collumns, type(rows)) #print de teste
    # collumns=int(inputMap.iloc[0,1])
    # print("Print da quantidade de linhas e colunas do mapa: ", rows, collumns);