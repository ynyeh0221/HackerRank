# no stdout for large testcase

# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
def cal_V(path):
    v = 0
    for i in xrange(1,N+1):
        temp = i
        for j in xrange(1, i):
            if path[j-1] >= path[i-1]:
                temp = i-j
        v += temp
    return v

T = int(raw_input())
for t in xrange(T):
    N = int(raw_input())
    Y = map(int, raw_input().split(' '))
    res = 0
    visited = [False for i in xrange(N)]
    totaltimes = 0
    for i in itertools.permutations(Y):
        res += cal_V(i)
        totaltimes += 1
    print "%.2f" % (res/float(totaltimes))
