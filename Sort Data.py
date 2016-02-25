# Enter your code here. Read input from STDIN. Print output to STDOUT
i1=raw_input().split(" ")
N=int(i1[0])
M=int(i1[1])
table=[]
for i in xrange(N):
    table.append(raw_input().split(" "))
    table[i]=map(int, table[i])
k=int(raw_input())
table=sorted(table, key=lambda x: x[k])
for i in xrange(N):
    print " ".join(map(str,table[i]))
