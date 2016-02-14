"""
 Check if linked list has cycle
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = ne   xt_node:

else:

 return 0 if no cycle else return 1
"""

def HasCycle(head):
    T={}
    while(head!=None):
        if head not in T.keys():
            T[head]=1
        else:
            return 1
        head=head.next
    return 0
        
  
  
  
  
  
  
