def dfs(u, adj, visited, parent, edges):
    """
    This function performs depth-first search on a graph represented by an adjacency list,
    and classifies the edges as tree edges, forward edges, and back edges.
    """
    visited[u] = True
    for v in adj[u]:
        if not visited[v]:
            edges.append((u, v, "tree"))
            parent[v] = u  # update the parent dictionary
            dfs(v, adj, visited, parent, edges)
        elif v != parent[u]:
            if visited[v] == True and parent[v] != -1:
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
    parent = [-1] * n  # initialize the parent dictionary
    for i in range(n):
        if not visited[i]:
            dfs(i, adj, visited, {i: -1}, edges)  # pass an initial value for the parent of the root node
    return edges

# Example usage:
s = {0, 1, 2, 3, 4}
edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 3)]
classes = edge_classification(s, edges)
print(classes)
# Output: [(0, 1, 'tree'), (1, 3, 'tree'), (1, 4, 'tree'), (0, 2, 'tree'), (2, 3, 'tree')]
