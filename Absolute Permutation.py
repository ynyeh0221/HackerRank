# Enter your code here. Read input from STDIN. Print output to STDOUT

T=int(raw_input())
for t in xrange(T):
    s=raw_input().split()
    N=int(s[0])
    K=int(s[1])
    number=[]
    
    for i in xrange(1,N+1):
        number.append(i)
    if K==0:
        print " ".join(str(e) for e in number)
    else:
        if N % (2*K)==0:
            for j in xrange(0,N/(2*K)):
                for i in xrange(1,K+1):
                    temp=number[j*2*K+i-1]
                    number[j*2*K+i-1]=number[j*2*K+i+K-1]
                    number[j*2*K+i+K-1]=temp
            print " ".join(str(e) for e in number)
        else:
            print -1
                
