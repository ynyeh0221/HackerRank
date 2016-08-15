# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
s1 = map(int, raw_input().split(' '))
s2 = map(int, raw_input().split(' '))
if sum(s1) != sum(s2):
    print -1
else:
    s1 = sorted(s1)
    s2 = sorted(s2)
    res = 0
    for i in xrange(len(s1)):
        if s1[i] > s2[i]:
            res += s1[i] - s2[i]
    print res
