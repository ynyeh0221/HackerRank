length=int(raw_input())
s=set(map(int, raw_input().split()))
N=int(raw_input())

for i in range(N):
    (p, q)=raw_input().split()
    s2=set(map(int, raw_input().split()))
    if p=='intersection_update':
        s.intersection_update(s2)
    elif p=='update':
        s.update(s2)
    elif p=='symmetric_difference_update':
        s.symmetric_difference_update(s2)
    elif p=='difference_update':
        s.difference_update(s2)
print sum(s)
