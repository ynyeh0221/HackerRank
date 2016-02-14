#Body
"""
 Compare two linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def CompareLists(headA, headB):
    check=0
    while(headA!=None and headB!=None):
        if headA.data!=headB.data:
            check=1
            break
        headA=headA.next
        headB=headB.next
    if headA!=None or headB!=None:
        return 0
    if check==1:
        return 0
    if check==0:
        return 1
  
  
  
  
  
  
  
  
