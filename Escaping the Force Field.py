# Didn't pass testcase 2

import math
import sys

def determinant(l):
    n=len(l)
    if (n>2):
        i=1
        t=0
        sum=0
        while t<=n-1:
            d={}
            t1=1
            while t1<=n-1:
                m=0
                d[t1]=[]
                while m<=n-1:
                    if (m==t):
                        u=0
                    else:
                        d[t1].append(l[t1][m])
                    m+=1
                t1+=1
            l1=[d[x] for x in d]
            sum=sum+i*(l[0][t])*(determinant(l1))
            i=i*(-1)
            t+=1
        return sum
    else:
        return (l[0][0]*l[1][1]-l[0][1]*l[1][0])


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

N = int(raw_input())
M = int(raw_input())

s = map(float, raw_input().split())
delta = Point(s[0],s[1],s[2])

area = []
for i in xrange(N):
    area += [map(int, raw_input().split())]
    
enemy = []
for i in xrange(M):
    s = map(float, raw_input().split())
    e = Point(s[0],s[1],s[2])
    enemy += [e]

dist = []
for i in xrange(N):
    p1 = enemy[area[i][0]]
    p2 = enemy[area[i][1]]
    p3 = enemy[area[i][2]]
    l = (p2.y - p1.y) * (p3.z - p1.z) - (p3.y - p1.y) * (p2.z - p1.z)
    m = (p2.z - p1.z) * (p3.x - p1.x) - (p3.z - p1.z) * (p2.x - p1.x)
    n = (p2.x - p1.x) * (p3.y - p1.y) - (p3.x - p1.x) * (p2.y - p1.y)
    t = (l * (p1.x - delta.x) + m * (p1.y - delta.y) + n * (p1.z - delta.z)) / (l*l + m*m + n*n)
    X = delta.x + t * l
    Y = delta.y + t * m
    Z = delta.z + t * n
    nn = max(math.fabs(l),math.fabs(m),math.fabs(n))
    if nn == math.fabs(n):
        M1 = [[X,Y,1],[p2.x,p2.y,1],[p3.x,p3.y,1]]
        M2 = [[p1.x,p1.y,1],[X,Y,1],[p3.x,p3.y,1]]
        M3 = [[p1.x,p1.y,1],[p2.x,p2.y,1],[X,Y,1]]
    elif nn == math.fabs(l):
        M1 = [[1,Y,Z],[1,p2.y,p2.z],[1,p3.y,p3.z]]
        M2 = [[1,p1.y,p1.z],[1,Y,Z],[1,p3.y,p3.z]]
        M3 = [[1,p1.y,p1.z],[1,p2.y,p2.z],[1,Y,Z]]
    elif nn == math.fabs(m):
        M1 = [[X,1,Z],[p2.x,1,p2.z],[p3.x,1,p3.z]]
        M2 = [[p1.x,1,p1.z],[X,1,Z],[p3.x,1,p3.z]]
        M3 = [[p1.x,1,p1.z],[p2.x,1,p2.z],[X,1,Z]]
        
    if math.fabs(determinant(M1)) + math.fabs(determinant(M2)) + math.fabs(determinant(M3)) == math.fabs(nn):
        min_dist = math.sqrt((X-delta.x)**2 + (Y-delta.y)**2 + (Z-delta.z)**2)
        dist += [min_dist]
    else:
        pA = delta
        pB = p2
        pC = p3
        SAB = math.sqrt((pA.x - pB.x)**2 + (pA.y - pB.y)**2 + (pA.z - pB.z)**2)
        SAC = math.sqrt((pA.x - pC.x)**2 + (pA.y - pC.y)**2 + (pA.z - pC.z)**2)
        SBC = math.sqrt((pC.x - pB.x)**2 + (pC.y - pB.y)**2 + (pC.z - pB.z)**2)
        p = (SAB + SAC + SBC) / 2.0
        S = math.sqrt(p * (p - SAB) * (p - SAC) * (p - SBC))
        h1 = (2 * S) / SBC
        
        pA = delta
        pB = p1
        pC = p3
        SAB = math.sqrt((pA.x - pB.x)**2 + (pA.y - pB.y)**2 + (pA.z - pB.z)**2)
        SAC = math.sqrt((pA.x - pC.x)**2 + (pA.y - pC.y)**2 + (pA.z - pC.z)**2)
        SBC = math.sqrt((pC.x - pB.x)**2 + (pC.y - pB.y)**2 + (pC.z - pB.z)**2)
        p = (SAB + SAC + SBC) / 2.0
        S = math.sqrt(p * (p - SAB) * (p - SAC) * (p - SBC))
        h2 = (2 * S) / SBC
        
        pA = delta
        pB = p1
        pC = p2
        SAB = math.sqrt((pA.x - pB.x)**2 + (pA.y - pB.y)**2 + (pA.z - pB.z)**2)
        SAC = math.sqrt((pA.x - pC.x)**2 + (pA.y - pC.y)**2 + (pA.z - pC.z)**2)
        SBC = math.sqrt((pC.x - pB.x)**2 + (pC.y - pB.y)**2 + (pC.z - pB.z)**2)
        p = (SAB + SAC + SBC) / 2.0
        S = math.sqrt(p * (p - SAB) * (p - SAC) * (p - SBC))
        h3 = (2 * S) / SBC
        
        dist += [min(h1, h2, h3)]
        
res = min(dist)
print "%.2f" % round(res,2)
print dist.index(res)
