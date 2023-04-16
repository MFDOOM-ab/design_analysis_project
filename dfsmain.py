graph = {
    '1': ['2', '3'],
    '2': ['1', '4', '5'],
    '3': ['1', '6', '7'],
    '4': ['2', '8'],
    '5': ['2', '9', '10'],
    '6': ['3', '11'],
    '7': ['3','8'],
    '8': ['4','7'],
    '9': ['5','3'],
    '10': ['5'],
    '11': ['6', '12'],
    '12': ['11']
}
visited = set() # Set to keep track of visited nodes of graph.
def dfs(visited, graph, node):  #function for dfs 
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
print("Following is the Depth-First Search")
dfs(visited, graph, '5')