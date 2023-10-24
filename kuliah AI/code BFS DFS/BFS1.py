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

visited = []
queue = []

def dfs(visited, graph, node, nodeEnd):
    visited.append(node)
    queue.append(node)
    while queue:
        m = queue.pop(0)
        print (m)
        if m == nodeEnd:
            sys.exit("Sudah sampai tujuan")
        for neighbour in graph[m]:
            if neighbour not in visited:    
                visited.append(neighbour)
                queue.append(neighbour)

print("The BFS traversal of the graph is ")
dfs(visited, graph, 'A', 'I')