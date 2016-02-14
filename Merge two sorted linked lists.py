"""
 Merge two linked lists
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""
def MergeLists(headA, headB):
    if headA==None:
        return headB
    elif headB==None:
        return headA
    dummy=Node(0,None)
    if headA.data>headB.data:
        dummy.next=headB
    else:
        dummy.next=headA
    p=dummy.next
    while (headA!=None and headB!=None):
        if headA.data>headB.data:
            c=headB
            headB=headB.next
        else:
            c=headA
            headA=headA.next
        p.next=c
        p=p.next
    if headA==None:
        p.next=headB
    else:
        p.next=headA
    return dummy.next


  
  
  
  
  
  
  
  
  
  
  
