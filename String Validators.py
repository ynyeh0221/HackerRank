# Enter your code here. Read input from STDIN. Print output to STDOUT
s = raw_input()
res = [False for i in xrange(5)]
for i in s:
    if i.isalnum():
        res[0] = True
    if i.isalpha():
        res[1] = True
    if i.isdigit():
        res[2] = True
    if i.islower():
        res[3] = True
    if i.isupper():
        res[4] = True
print '\n'.join(str(e) for e in res)
