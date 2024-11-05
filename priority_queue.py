class Node:
    val=0
    next=None
    priority=0
    def __init__(self,val,next,priority):
        self.val=val
        self.next=next
        self.priority=priority

class LinkedList:
    def __init__(self,head=None) -> None:
        self.head=head
        
    def insert(self,val,priority):
        new_node=Node(val,None,priority)
        if self.head == None:
            self.head=new_node
        elif self.head.priority<priority:
                new_node.next=self.head
                self.head=new_node
        else:
            curr=self.head
            while curr.next and curr.next.priority>=priority:
                    curr=curr.next
            new_node.next=curr.next
            curr.next=new_node
    
    def delete(self):
        if self.head==None:
            return
        self.head=self.head.next

class queue:
    queue_size=0
    def __init__(self,queue_size):
        self.queue_size=queue_size
        self.ans=LinkedList()
        self.size=0

    def enqueue(self,ele,priority):
        if self.size < self.queue_size:
            self.ans.insert(ele,priority)
            self.size+=1

    def dequeue(self):
        if self.size > 0:
            self.ans.delete()
            self.size-=1

    def print(self):
        curr=self.ans.head
        while curr:
            print(curr.val,end="->")
            curr=curr.next
        print()
                
                  
            
ans = queue(10)
ans.enqueue(15,1)
ans.enqueue(20,4)
ans.enqueue(30,3)
ans.print()
ans.enqueue(40,5)
ans.print()
ans.dequeue()
ans.print()
