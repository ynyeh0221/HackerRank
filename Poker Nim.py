# Enter your code here. Read input from STDIN. Print output to STDOUT
T=int(raw_input())
for i in xrange(T):
    t=raw_input().split()
    n=int(t[0])
    k=int(t[1])
    s=raw_input().split()
    nim=map(int,s)
    nimsum=nim[0]
    for j in xrange(1,n):
        nimsum=nim[j]^nimsum
    
    if nimsum==0:
        print "Second"
    else:
        print "First"
    
