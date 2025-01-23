from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.edges = []
        self.text = ""

class Graph:
    def __init__(self, size):
        self.nodes = [Node(i) for i in range(size)]
        print(self.nodes)
    def addEdge(self, u, v):
        self.nodes[u].edges.append(self.nodes[v])
        self.nodes[v].edges.append(self.nodes[u])

    def bfs_un(self):
        visited = set()
        for node in self.nodes:
            if node not in visited:
                self.find(node, visited)

    def find(self, start, visited):
        queue = deque([start])
        visited.add(start)
        while queue:
            current_node = queue.popleft()
            print(chr(current_node.data + 97), end=" ")
            for neighbor in current_node.edges:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

ans = Graph(5)
ans.addEdge(0, 1)
ans.addEdge(0, 2)
ans.addEdge(1, 3)
ans.addEdge(3, 4)
ans.bfs_un()
