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
dfs(visited, graph, '1', '9')