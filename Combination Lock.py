numfrom = map(int, raw_input().split(' '))
numto = map(int, raw_input().split(' '))
res = 0
for i in xrange(len(numfrom)):
    if numto[i] < numfrom[i]:
        res += min(numfrom[i] - numto[i], numto[i] + 10 - numfrom[i])
    else:
        res += min(numto[i] - numfrom[i], numfrom[i] + 10 - numto[i])
print res
