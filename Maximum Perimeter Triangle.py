from operator import itemgetter
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(raw_input())
s=raw_input().split()
num=map(int,s)
num=sorted(num)

result=[]
for i in xrange(n-1,-1,-1):
    for j in xrange(i-1,-1,-1):
        for k in xrange(j-1,-1,-1):
            if i!=j and j!=k and i!=k:
                if num[i]+num[j]>num[k] and num[i]+num[k]>num[j] and num[j]+num[k]>num[i]:
                    result.append([num[k],num[j],num[i]])
                    
result=sorted(result, key=itemgetter(2), reverse=True)
result=sorted(result, key=itemgetter(0), reverse=True)
if len(result)>0:
    print ' '.join(str(e) for e in result[0])
else:
    print -1
