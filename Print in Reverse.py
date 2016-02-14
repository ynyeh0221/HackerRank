"""
 Print elements of a linked list in reverse order as standard output
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 
"""

def ReversePrint(head):
    if head==None:
        return 0
    elif head.next==None:
        return head.data
    p1=head.next
    p2=head.next.next
    head.next=None
    while (p2!=None):
        p1.next=head
        head=p1
        p1=p2
        p2=p2.next
    p1.next=head
    while (p1!=None):
        print p1.data
        p1=p1.next
