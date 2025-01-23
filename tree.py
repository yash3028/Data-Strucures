import math
class Node:        
    def __init__(self,val):
        self.val=val
        self.child = [None]*3

class Tree:
    def __init__(self,max_size):
        self.max_size=max_size
        self.root=None
        self.size=0
    def insert(self,val):
        new_node=Node(val)
        if self.root==None:
            self.root = new_node
            self.size += 1
            return
        queue = [self.root]
        while len(queue):
            temp=queue.pop(0)
            for i in range(3):
                if temp.child[i]==None:
                    temp.child[i]=new_node
                    self.size+=1
                    return
                else:
                    queue.append(temp.child[i])

    def print(self):
        queue=[self.root]
        p=0
        nc=0
        while queue:
            temp=queue.pop(0)
            print(temp.val,end=" ")
            nc+=1
            if nc==math.pow(3,p):
                nc=0
                p+=1
            for i in temp.child:
                if i!= None:
                    queue.append(i)
            
ans=Tree(10)
ans.insert(10)
ans.insert(20)
ans.insert(30)
ans.insert(40)
ans.insert(201)
ans.insert(202)
ans.insert(203)
ans.insert(301)
ans.insert(302)
ans.insert(303)
ans.print()

