# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
dic = {}
for i in xrange(N):
    s = raw_input()
    if s not in dic:
        dic[s] = 0
    dic[s] += 1
Q = int(raw_input())
for i in xrange(Q):
    q = raw_input()
    if q in dic:
        print dic[q]
    else:
        print 0
