n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
c = map(int,raw_input().strip().split(' '))
E = 100
E -= 1
i = (0 + k) % n
if c[i] == 1:
    E -= 2
while i != 0:
    E -= 1
    i = (i + k) % n
    if c[i] == 1:
        E -= 2
print E
