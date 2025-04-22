import os

def printGraph():
    pass

def receberGraph(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    # Ler o número de vértices
    num_vertices = int(lines[0].strip())
    
    # Ler a lista de vértices
    vertices = list(map(int, lines[1].strip().split()))
    
    # Ler o número de arestas
    num_edges = int(lines[2].strip())
    
    # Inicializar o grafo como um dicionário de listas de tuplas (vizinho, peso)
    graph = {v: [] for v in vertices}
    
    # Ler as arestas e preencher o grafo
    for i in range(3, 3 + num_edges):
        edge_data = list(map(int, lines[i].strip().split()))
        if len(edge_data) >= 3:
            source, dest, weight = edge_data[0], edge_data[1], edge_data[2]
            graph[source].append((dest, weight))
    
    return num_vertices, vertices, num_edges


def escreverArquivoSaída(filename, vertices, num_vertices, num_edges):   

    with open(filename, 'w') as file:
        file.write(f'NumVertices={num_vertices}')

        for i in vertices:
            file.write(f'\nVertice: {i}')

        file.write(f'\nNumArestas={num_edges}')

# print(receberGraph('arq1.in.txt'))
num_vertices, vertices, num_edges = receberGraph('arq1.in.txt')

escreverArquivoSaída('arq2.out.txt', vertices, num_vertices, num_edges)