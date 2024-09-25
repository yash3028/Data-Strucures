class node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class stack:
    def __init__(self,max_size):
        self.max_size=max_size
        self.stacksize=0
        self.arr=[None]*max_size
    def push(self,val):
        if self.max_size==self.stacksize:
            return
        else:
            self.arr[self.stacksize]=val
            self.stacksize+=1
    def pop(self)->node:
        if self.stacksize==0:
            return 
        pop_ele=self.arr[self.stacksize-1]
        self.stacksize-=1
        return pop_ele

class bst:
    def __init__(self):
        self.root = None
        self.count=0

    def insert(self, val):
        if self.root==None:
            self.root=node(val)
            self.count+=1
            return
        parent=None
        temp=self.root
        while temp!=None:
            parent=temp
            if temp.val>val:
                temp=temp.left
            else:
                temp=temp.right
        if parent.val>val:
            parent.left=node(val)
        else:
            parent.right=node(val)
        self.count+=1
        return self.root

    def delete(self,val):
        if self.root==None:
            return None
        temp=self.root
        parent=None
        while temp!=None:
            parent=temp
            if temp.val>val:
                temp=temp.left
            else:
                temp=temp.right
            if parent.left==val:
                parent.left=None
            else:
                parent.right=None
        self.count-=1
        return self.root
    
    def preorder(self):
        arr=[]
        sta=stack(self.count)
        if self.root==None:
            return 
        temp=self.root
        sta.push(temp)
        while sta.stacksize!=0:
            curr_node=sta.pop()
            print(curr_node.val,end=" ")

            if curr_node.right!=None:
                sta.push(curr_node.right)
            if curr_node.left!=None:
                sta.push(curr_node.left)

    def search(self,val):
        if self.root==None:
            return None
        temp = self.root
        while temp!=None:
            if temp.val==val:
                return True
            elif temp.val>val:
                temp=temp.left
            else:
                temp=temp.right
        return False
    
ans = bst()
ans.insert(10)
print(ans.root.val)
ans.insert(20)
print(ans.count)
ans.insert(5)
ans.insert(7)
ans.insert(4)
ans.insert(25)
ans.preorder()




    


        