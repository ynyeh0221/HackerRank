# Didn't pass testcase 11, 15

import sys

def dfs(p, s, dic, ind, path):
    global cost
    global r
    global ncr
    
    if r:
        return
    if len(path) > len(ncr):
        ncr = path[:]
    if ind == len(p):
        delete = 0
        add = 0
        path.pop(0)
        pathcopy = path[:]
        stack = []
        while path:
            temp = path.pop(0)
            if not stack:
                stack += [temp]
            elif temp[0] > stack[-1][1]:
                delete += temp[0] - stack[-1][1] - 1
            else:
                add += stack[-1][1] - temp[0] + 1
            stack += [temp]
        delete += stack[0][0] + len(s) - stack[-1][1] - 1
        if not r:
            cost = delete + add + len(p)-1
            r = pathcopy[:]
        return
    if not r:
        for j in dic[p[ind]]:
            if j > path[-1][0]:
                dfs(p, s, dic, ind + 1, path + [[j, j+len(p[ind])-1]])

s = raw_input()
p = raw_input().split()
dic = {}
for pp in p:
    if pp not in dic:
        dic[pp] = []
    for i in xrange(len(s)):
        if i+len(pp) <= len(s) and s[i:i+len(pp)] == pp:
            dic[pp] += [i]

global cost
global r
global ncr
mincost = sys.maxint
r = []
ncr = []
dfs(p, s, dic, 0, [[-1,-1]])
if r:
    print "YES"
    ss = ""
    for i in xrange(len(r)):
        if ss != "":
            ss += " "
        ss += p[i] + " " + " ".join(str(e) for e in r[i])
    print ss
    print cost
else:    
    print "NO"
    ss = ""
    ncr.pop(0)
    for i in xrange(len(ncr)):
        if ss != "":
            ss += " "
        ss += p[i] + " " + " ".join(str(e) for e in ncr[i])
    print ss if ss != "" else 0
    print 0
