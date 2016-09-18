class Node:
    def __init__(self,info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

class bst:
    def __init__(self):
        self.root = None

    def create(self,val):
        if self.root == None:
            self.root = Node(val)
        else:
            cur = self.root
            while 1:
                if val < cur.info:
                    if cur.left:
                        cur = cur.left
                    else:
                        cur.left = Node(val)
                        break
                elif val > cur.info:                 
                    if cur.right:
                        cur = cur.right
                    else:
                        cur.right = Node(val)
                        break
                else:
                    break 

    def BF(self):
        self.root.level = 0
        queue = [self.root]
        output = []
        cur_level = self.root.level
        
        while len(queue) > 0:                 
            cur = queue.pop(0) 
            if cur.level > cur_level:
                cur_level += 1
                output += ["\n"]
            output += [str(cur.info) + " "]

            if cur.left:
                cur.left.level = cur_level + 1
                queue += [cur.left]                  

            if cur.right:
                cur.right.level = cur_level + 1
                queue += [cur.right]                    
        return "".join(output)   

N = int(raw_input())
s = map(int, raw_input().split())
t = bst()     
for i in s:
    t.create(i)
res = t.BF().split("\n")
F = 0
for i in xrange(len(res)):
    res[i] = res[i].split()
    F += len(res[i]) * i
print F
