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
dfs(visited, graph, '0', '7')