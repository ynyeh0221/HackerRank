"""
 Delete duplicate nodes
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def RemoveDuplicates(head):
    dummy=Node(0,head)
    p=dummy
    T=[]
    while(head!=None):
        if head.data not in T:
            T.append(head.data)
        head=head.next
    for j in xrange(0,len(T)):
        temp=Node(T[j],None)
        p.next=temp
        p=p.next
    return dummy.next
  
  
  
  
  
