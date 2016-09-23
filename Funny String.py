# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
for n in xrange(N):
    s = raw_input()
    r = s[::-1]
    funny = True
    for i in xrange(1, len(s)):
        if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(r[i]) - ord(r[i-1])):
            funny = False
            break
    print "Funny" if funny else "Not Funny"
