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
        for char in element:
            idx = self.index(char)
            if not head.child[idx]:
                head.child[idx] = self.getNode()
            head = head.child[idx]
        head.end = True

    def search(self, element):
        head = self.root
        n = len(element)
        for char in element:
            idx = self.index(char)
            if not head.child[idx]:
                return False
            head = head.child[idx]  
        return head.end
    def empty(self,root):
        for i in root.child:
            if i!=None:
                return False
        return True
    def delete(self, element):
        stack = []
        head = self.root
        for char in element:
            idx = self.index(char)
            if not head.child[idx]:
                return False
            stack.append((head, idx))
            head = head.child[idx]
        if not head.end:  
            return False
        head.end = False  
        while stack:
            parent, idx = stack.pop()
            if self.empty(head) and not head.end:
                parent.child[idx] = None
            else:
                break
            head = parent
        return True



ans = Trie()
ans.insert('yash')
ans.insert('wanth')
ans.insert('reddy')
print(ans.search('wanth'))  
ans.insert('bqvd')
print(ans.search('bqvd'))   
print(ans.search('missing'))  
ans.delete('wanth')
print(ans.search('wanth'))