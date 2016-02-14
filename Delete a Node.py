"""
 Delete Node at a given position in a linked list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""

def Delete(head, position):
    dummy1=Node(0,head)
    if position==0:
        dummy1.next=head.next
        head.next=None
    else:
        for i in xrange(0,position-1):
            head=head.next
        head.next=head.next.next
    return dummy1.next
