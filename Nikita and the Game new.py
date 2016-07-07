# Enter your code here. Read input from STDIN. Print output to STDOUT
def summation(l, r):
    return A[r] - A[l-1]

def get(l, r, s):
    low = l
    high = r
    while low <= high:
        mid = (low + high) / 2
        x = summation(l, mid)
        if x == s and (mid == 1 or summation(l, mid-1) != s):
            return mid
        elif x >= s:
            high = mid - 1
        else:
            low = mid + 1
    return -1

def helper(l, r):
    s = summation(l, r)
    if l != r and s % 2 == 0:
        ind = get(l, r, s/2)
        if ind != -1:
            return max(helper(l, ind), helper(ind+1, r)) + 1;
    return 0
            
M = int(raw_input())
for m in xrange(M):
    n = int(raw_input())
    A = map(int, raw_input().split(' '))
    if all(v == 0 for v in A):
        print n-1
    else:
        A.insert(0, 0)
        for i in xrange(1,n+1):
            A[i] += A[i-1]
        print helper(1, n)
