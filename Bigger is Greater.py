def nextPermutation(a):
    if len(a) <= 1:
        return a
    partition = -1
    for i in range(len(a)-2, -1, -1):
        if a[i] < a[i+1]:
            partition = i
            break
    if partition == -1: 
        a.reverse()
        return a
    else:
        for i in range(len(a)-1, partition, -1):
            if a[i] > a[partition]:
                a[i], a[partition] = a[partition], a[i]
                break
    left = partition+1; right = len(a)-1
    while left < right:
        a[left], a[right] = a[right], a[left]
        left += 1
        right -= 1
    return ''.join(a)

T = int(raw_input())
for t in xrange(T):
    s = list(raw_input())
    res = nextPermutation(s)
    if res == s:
        print 'no answer'
    else:
        print res
