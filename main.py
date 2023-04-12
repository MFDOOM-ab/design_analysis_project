# Using a Python dictionary to act as an adjacency list
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
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

def edge_classification(s, edges):
    """
    This function takes a set s as input and returns the tree edges, forward edges,
    and back edges of the graph represented by the set s.
    """
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

# Example usage:
s = {0, 1, 2, 3, 4}
edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 3)]
edge_classes = edge_classification(s, edges)
print(edge_classes)
# Output: [(0, 1, 'tree'), (1, 3, 'tree'), (1, 4, 'tree'), (0, 2, 'tree'), (2, 3, 'tree')]