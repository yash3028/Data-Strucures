from collections import deque

def add(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

def shortest_path(adj, s, e):
    v = len(adj)
    dist = [float('inf')] * v
    visit = [False] * v
    
    q = deque([s])
    dist[s] = 0
    visit[s] = True

    while q:
        u = q.popleft()
        for v in adj[u]:
            if not visit[v]:
                dist[v] = dist[u] + 1
                visit[v] = True
                q.append(v)
                if v == e:
                    return dist[v]

    return -1

v = 8
adj = [[] for _ in range(v)]

add(adj, 0, 1)
add(adj, 0, 3)
add(adj, 1, 2)
add(adj, 3, 4)
add(adj, 3, 7)
add(adj, 4, 5)
add(adj, 4, 6)
add(adj, 4, 7)
add(adj, 5, 6)
add(adj, 6, 7)

start = 0
end = 7
cost = shortest_path(adj, start, end)
print(cost)