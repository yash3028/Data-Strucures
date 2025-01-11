class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.end = False

class Trie:
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def index(self, char):
        return ord(char) - ord('a')

    def insert(self, element):
        head = self.root
        n = len(element)
        for char in range(n):
            idx = self.index(element[char])
            if not head.child[idx]:
                head.child[idx] = self.getNode()
            head = head.child[idx]
        head.end = True

    def search(self, element):
        head = self.root
        n = len(element)
        for char in range(n):
            idx = self.index(element[char])
            if not head.child[idx]:
                return False
            head = head.child[idx]  
        return head.end
ans = Trie()
ans.insert('yash')
ans.insert('wanth')
ans.insert('reddy')
print(ans.search('wanth'))  
ans.insert('bqvd')
print(ans.search('bqvd'))   
print(ans.search('missing'))  
