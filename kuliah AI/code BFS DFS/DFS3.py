import sys, traceback

graph = {
    '0' : ['3', '4'],
    '1' : ['0', '6'],
    '2' : ['5', '6'],
    '3' : ['7', '1'],
    '4' : ['6'],
    '5' : ['7', '6'],
    '6' : ['2', '4'],
    '7' : ['5'],
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
dfs(visited, graph, '0', '7')