def rotate(a):
    return [a[2]] + a[:2] 

T = int(raw_input())
for i in xrange(T):
    N = int(raw_input())
    a = map(int, raw_input().split())
    for i in xrange(N-2):
        for j in xrange(N-3, i-1, -1):
            if a[j+2] <= a[j+1] and a[j+2] <= a[j]:
                a[j:j+3] = rotate(a[j:j+3])[:]
            elif a[j+1] <= a[j] and a[j+1] <= a[j + 2]:
                a[j:j+3] = rotate(a[j:j+3])[:]
                a[j:j+3] = rotate(a[j:j+3])[:]
    if a[-1] == a[-2] + 1:
        print 'YES'
    else:
        print 'NO'
