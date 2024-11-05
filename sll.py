class ListNode:
    def __init__(self,val=None,next=None):
        self.val=val
        self.next=next
class LinkedList:
    def __init__(self,head=None):
        self.head=head
    
    def insert(self,val):
        new=ListNode(val)
        if not self.head:
            self.head = new
            return
        curr=self.head
        while curr.next:
           curr=curr.next
        curr.next=new
    
    def insertMiddle(self,val,curr):
        if curr is None:
            return
        new=ListNode(val)
        new.next=curr.next
        curr.next=new

    def print(self):
        curr=self.head
        while curr:
            print(curr.val,end="->")
            curr=curr.next
        print()
   
    def deleteEnd(self):
        if not self.head:
            return
        curr=self.head
        if not curr.next:
            self.head=None
            return
        while curr.next.next:
            curr=curr.next
        curr.next=None 

linked_list = LinkedList()
linked_list.insert(18)
linked_list.insert(6)
linked_list.insert(10)
linked_list.insert(3)
linked_list.print()

