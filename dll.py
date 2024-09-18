import math
from typing import Optional
class ListNode:
    val=0
    next=None
    prev=None
    def __init__(self,val,next=None,prev=None):
        self.val=val
        self.next=next
        self.prev=prev
             
class LinkedList:
    def __init__(self,head):
        self.head=head


    def insert(self, val):
        new_node = ListNode(val)
        if not self.head:  # If the list is empty
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr

    def insertMiddle(self, val, curr):
        new_node = ListNode(val)
        new_node.next = curr.next
        if curr.next:
            curr.next.prev = new_node
        curr.next = new_node
        new_node.prev = curr

    def print(self):
        curr = self.head
        while curr:
            print(curr.val, end=" <-> ")
            curr = curr.next
        print()

    def deleteEnd(self):
        if not self.head:
            return

        curr = self.head
        if not curr.next:
            self.head = None
            return
        
        while curr.next:
            curr = curr.next
linked_list = LinkedList(None)

linked_list.insert(18)
linked_list.insert(6)
linked_list.insert(10)
linked_list.insert(3)
linked_list.print()


