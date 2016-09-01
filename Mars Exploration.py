import sys

S = raw_input().strip()
res = 0
sos = 'SOS'
for i in xrange(0, len(S), 3):
    for j in xrange(3):
        if S[i+j] != sos[j]:
            res += 1
print res
