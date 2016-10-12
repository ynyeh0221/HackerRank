[n,m] = map(int, raw_input().split())
a = map(int, raw_input().split())
A = set(map(int, raw_input().split()))
B = set(map(int, raw_input().split()))
happiness = 0
for i in a:
    if i in A:
        happiness += 1
    elif i in B:
        happiness -= 1
print happiness
