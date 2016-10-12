"""
 Find the node at which both lists merge and return the data of that node.
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 
"""

def FindMergeNode(headA, headB):
    p1 = headA
    p2 = headB
    len1 = len2 = 0
    while p1:
        len1 += 1
        p1 = p1.next
    while p2:
        len2 += 1
        p2 = p2.next
    if len1 > len2:
        for i in xrange(len1 - len2):
            headA = headA.next
    else:
        for i in xrange(len2 - len1):
            headB = headB.next
    while headA and headB:
        if headA == headB:
            return headA.data
        headA = headA.next
        headB = headB.next 
