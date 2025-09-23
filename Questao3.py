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