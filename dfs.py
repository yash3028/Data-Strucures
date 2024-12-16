def dfs(adj, s, visited=None):
    if visited is None:
        visited = [False] * len(adj)

    visited[s] = True
    print(s, end=" ")

    for x in adj[s]:
        if not visited[x]:
            dfs(adj, x, visited)

def add_edge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

V = 5
adj = [[] for _ in range(V)]
add_edge(adj, 0, 1)
add_edge(adj, 0, 2)
add_edge(adj, 1, 3)
add_edge(adj, 1, 4)
add_edge(adj, 2, 4)
dfs(adj, 0)
