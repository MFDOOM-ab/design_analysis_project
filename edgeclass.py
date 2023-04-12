# DFS Function with adjacent list to classify edges

def dfs(u, adj, visited, parent, edges):

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
