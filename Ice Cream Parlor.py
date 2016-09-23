# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(raw_input())
for tt in xrange(t):
    m = int(raw_input())
    n = int(raw_input())
    price = map(int, raw_input().split())
    dic = {}
    for i in xrange(n):
        if m - price[i] in dic:
            print ' '.join(str(e) for e in sorted([dic[m - price[i]]+1, i+1]))
            break
        if price[i] not in dic:
            dic[price[i]] = i
