from collections import deque
class node:
    data=0
    edges=[] #(0,1)
    def __init__(self,data):
        self.data=data
        self.edges=[]
class Graph:
    def __init__(self,size,arr):
        for i in range(size):
            arr.append(node(i))
        self.nodes=arr
    def addEdge(self,u,v):
        self.nodes[u].edges.append(v)
        self.nodes[v].edges.append(u)
    def bfs_un(self):
        visited = set()
        for node in range(len(self.nodes)):
            if node not in visited:
                self.find(node, visited)
    def find(self, start, visited):
        queue = deque([start])
        visited.add(start)
        while queue:
            node = queue.popleft()
            print(node, end=" ")
            for neighbor in self.nodes[node].edges:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=" ")
        for neighbor in self.nodes[start].edges:
            if neighbor not in visited:
                self.dfs(neighbor, visited)
    def dfs_un(self):
        visited = set()
        for node in range(len(self.nodes)):
            if node not in visited:
                self.dfs(node, visited)
arr=[]
ans=Graph(10,arr)
ans.addEdge(0, 1)
ans.addEdge(0, 2)
ans.addEdge(1, 3)
ans.addEdge(4, 5)
ans.bfs_un()
print()
ans.dfs_un()