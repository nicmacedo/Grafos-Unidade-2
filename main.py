import os


def printGraph():
    pass


def receberGraph(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    # Read the number of vertices
    num_vertices = int(lines[0].strip())
    
    # Read the list of vertices
    vertices = list(map(int, lines[1].strip().split()))
    
    # Read the number of edges
    num_edges = int(lines[2].strip())
    
    # Initialize the graph as a dictionary of lists of tuples (neighbor, weight)
    graph = {v: [] for v in vertices}
    
    # Read the edges and populate the graph
    for i in range(3, 3 + num_edges):
        edge_data = list(map(int, lines[i].strip().split()))
        if len(edge_data) >= 3:
            source, dest, weight = edge_data[0], edge_data[1], edge_data[2]
            graph[source].append((dest, weight))
    
    return graph

print(receberGraph('arq1.in.txt'))