# Enter your code here. Read input from STDIN. Print output to STDOUT
i1=raw_input().split(" ")
S=int(i1[0])
P=int(i1[1])
score=[[0 for x in range(S)] for x in range(P)]
X=[]
for i in xrange(P):
    score[i]=map(float,raw_input().split())
    X+=[score[i]]
avg=[]
for i in xrange(S):
    avg.append(sum(zip(*X)[i])/P)
    print avg[i]
