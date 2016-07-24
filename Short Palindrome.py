# timeout

# Enter your code here. Read input from STDIN. Print output to STDOUT

mod = pow(10, 9) + 7
s = raw_input()
res = 0

for i in xrange(len(s)):
    for j in xrange(i+1, len(s)):
        for k in xrange(j+1, len(s)):
            if s[j] == s[k]:
                res += s[k+1:].count(s[i])
print res % mod
