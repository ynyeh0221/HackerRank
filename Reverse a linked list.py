"""
 Reverse a linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def Reverse(head):
    if head==None:
        return head
    elif head.next==None:
        return head
    p1=head.next
    p2=head.next.next
    head.next=None
    while (p2!=None):
        p1.next=head
        head=p1
        p1=p2
        p2=p2.next
    p1.next=head
    return p1

  
  
  
  
  
  
