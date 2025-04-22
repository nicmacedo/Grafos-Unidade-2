import os


def printGraph():
    pass


def receberGraph(self, filename):
    with open(filename, 'r') as file:
        lines = file.read()

    # Read the number of vertices and edges
    num_vertices, num_edges = map(int, lines[0].strip().split())

    # Initialize the graph as a dictionary of lists
    graph = {i: [] for i in range(num_vertices)}

    # Read the edges and populate the graph
    for line in lines[1:num_edges + 1]:
        u, v = map(int, line.strip().split())
        graph[u].append(v)
        graph[v].append(u)  # Assuming undirected graph

    return graph