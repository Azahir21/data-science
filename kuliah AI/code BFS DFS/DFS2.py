import sys, traceback

graph = {
    '1' : ['2', '3'],
    '2' : ['4', '5'],
    '3' : ['4', '6'],
    '4' : ['5', '7', '8', '6'],
    '5' : ['7'],
    '6' : ['9'],
    '7' : ['9'],
    '8' : ['9'],
    '9' : [''],
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
dfs(visited, graph, '1', '9')