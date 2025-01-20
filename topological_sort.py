from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def edge(self, u, v):
        self.graph[u].append(v)  

    def topo(self):
        degree = [0] * self.V

        for i in self.graph:
            for j in self.graph[i]:
                degree[j] += 1

        queue = []
        for i in range(self.V):
            if degree[i] == 0:
                queue.append(i)  

        cnt = 0
        res = []

        while queue:
            left = queue.pop(0)  
            res.append(left)

            for i in self.graph[left]:
                degree[i] -= 1
                if degree[i] == 0:
                    queue.append(i)

            cnt += 1

        if cnt != self.V:
            return False 
        else:
            return res  

g = Graph(6)
g.edge(5, 2)
g.edge(5, 0)
g.edge(4, 0)
g.edge(4, 1)
g.edge(2, 3)
g.edge(3, 1)

print(g.topo())  
