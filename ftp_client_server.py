"""
    Double Link List

    In computer science, a doubly linked list
    is a linked data structure that consists
    of a set of sequentially linked records
    called nodes. Each node contains two fields, 
    called links, that are references to the previous
    and to the next node in the sequence of nodes.

    More Info : https://en.wikipedia.org/wiki/Doubly_linked_list
"""

class Node(object):
 
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next
 
 
class DoubleList(object):
 
    head = None
    tail = None
 
    def append(self, data):
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node
 
    def remove(self, node_value):
        current_node = self.head
 
        while current_node is not None:
            if current_node.data == node_value:
                # if it's not the first element
                if current_node.prev is not None:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                else:
                    # otherwise we have no prev (it's None), 
                    # head is the next one, and prev becomes None
                    self.head = current_node.next
                    current_node.next.prev = None
 
            current_node = current_node.next
 
    def show(self):
        print "Show list data:"
        current_node = self.head
        while current_node is not None:
            print current_node.prev.data if hasattr(current_node.prev, "data") else None,
            print current_node.data,
            print current_node.next.data if hasattr(current_node.next, "data") else None
 
            current_node = current_node.next
        print "*"*50
 
 
DoubleLinkList = DoubleList()

DoubleLinkList.append(5)
DoubleLinkList.append(6)

DoubleLinkList.append(50)
DoubleLinkList.append(30)

DoubleLinkList.show()
DoubleLinkList.remove(50)

DoubleLinkList.remove(5)
DoubleLinkList.show()