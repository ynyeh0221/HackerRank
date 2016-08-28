s = raw_input().split(' ')
n = int(s[0])
k = int(s[1])
c = map(int, raw_input().split(' '))
b = int(raw_input())
ss = sum(c) - c[k]
fair = ss/2
if fair == b:
    print 'Bon Appetit'
else:
    print b - fair
