import sys, traceback

graph = {
    'A' : ['B', 'C'],
    'B' : ['H'],
    'C' : ['D', 'E'],
    'D' : ['F', 'G'],
    'E' : ['I'],
    'F' : ['H'],
    'G' : ['I'],
    'H' : ['I'],
    'I' : [],
}

visited = set()

def dfs(visited, graph, node, nodeEnd):
    if node not in visited:
        print (node)
        visited.add(node)
        if node == nodeEnd:
            sys.exit("Sudah sampai tujuan")
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour, nodeEnd)

print("The DFS traversal of the graph is ")
dfs(visited, graph, 'A', 'I')