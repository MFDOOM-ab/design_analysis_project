graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

# Function to track visited nodes

visited = set() 

# Depth First Search stores visited nodes
def dfs(visited, graph, node): 
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


print("Following is the Depth-First Search")
dfs(visited, graph, '5')

# DFS Function with adjacent list to classify edges

def dfs(u, adj, visited, parent, edges):
    """
    This function performs depth-first search on a graph represented by an adjacency list,
    and classifies the edges as tree edges, forward edges, and back edges.
    """
    visited[u] = True
    for v in adj[u]:
        if not visited[v]:
            edges.append((u, v, "tree"))
            dfs(v, adj, visited, u, edges)
        elif v != parent[u]:
            if visited[v] == True and v in parent:
                edges.append((u, v, "back"))
            else:
                edges.append((u, v, "forward"))

def edgeClass(s, edges):

    n = len(s)
    adj = {}
    for i in range(n):
        adj[i] = set()
    for e in edges:
        adj[e[0]].add(e[1])
        adj[e[1]].add(e[0])
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            dfs(i, adj, visited, {}, edges)
    return edges

# EXAMPLE -
s = {0, 1, 2, 3, 4}
edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 3)]
print(edgeClass(s,edges))
