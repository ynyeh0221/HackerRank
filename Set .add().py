# Enter your code here. Read input from STDIN. Print output to STDOUT
N=int(raw_input())
s=set()
for i in xrange(N):
    s.add(raw_input())
print len(s)
