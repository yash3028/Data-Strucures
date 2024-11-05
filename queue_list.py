class Node:
    val=0
    next=None
    def __init__(self,val,next):
        self.val=val
        self.next=next
    
class LinkedList:
    def __init__(self,head=None,tail=None) -> None:
        self.head=head
        self.tail=tail
        
    def insert(self,val):
        if self.head == None:
            self.head=Node(val,None)
            self.tail=self.head
        else:
            new_node=Node(val,None)
            self.tail.next=new_node
            self.tail=self.tail.next
    
    def delete(self):
        if self.head==None:
            return
        self.head=self.head.next

    def print(self):
        curr=self.head
        while curr:
            print(curr.val,end="->")
            curr=curr.next
        print()

class queue:
    queue_size=0
    def __init__(self,queue_size):
        self.queue_size=queue_size
        self.size=0
        self.ans=LinkedList()
    
    def enqueue(self,ele):
        if self.size<self.queue_size:
            self.ans.insert(ele)
            self.size+=1
            
    
    def deqeue(self):
        if self.size>0:
            res= self.ans.delete()
            self.size-=1
            return res
        
    def print(self):
        curr=self.ans.head
        while curr:
            print(curr.val,end="->")
            curr=curr.next
        print()

        





ans = queue(10)
ans.enqueue(10)
ans.enqueue(20)
ans.enqueue(30)
ans.print()
ans.enqueue(40)
ans.print()

print(ans.deqeue())
ans.print()


