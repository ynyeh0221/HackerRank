n = input()
s = set(map(int, raw_input().split()))
m=int(raw_input())
for i in xrange(m):
    p=raw_input().split()
    if p[0]=="remove":
        s.remove(int(p[1]))
    elif p[0]=="discard":
        s.discard(int(p[1]))
    else:
        s.pop()
print sum(list(s))
