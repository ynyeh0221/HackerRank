s = raw_input().lower()
score1 = score2 = 0
for i in xrange(len(s)):
    if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
        score2 += len(s)-i
    else:
        score1 += len(s)-i
if score1 > score2:
    print 'Stuart ' + str(score1)
elif score1 < score2:
    print 'Kevin ' + str(score2)
else:
    print 'Draw'
