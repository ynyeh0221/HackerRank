# Enter your code here. Read input from STDIN. Print output to STDOUT
q = int(raw_input())
for qq in xrange(q):
    a = raw_input()
    b = raw_input()
    dic = {}
    result = False
    for i in b:
        if i not in dic:
            dic[i] = 0
        dic[i] += 1
    for i in a:
        if i not in dic:
            if i == i.upper():
                print 'NO'
                result = True
                break
        else:
            if dic[i] > 0:
                dic[i] -= 1
            else:
                print 'NO'
                result = True
                break
    if result:
        continue
    a = a.upper()
    T = ['' for i in xrange(len(a)+1)]
    for i in xrange(1, len(a)+1):
        temp = ''
        for j in xrange(i):
            if len(T[j] + a[i-1]) > len(temp):
                temp = T[j] + a[i-1]
                if temp == b[:len(temp)]:
                    T[i] = temp
                    if len(temp) == len(b):
                        print "YES"
                        result = True
                        break
        if result:
            break
    if not result:
        print 'NO'
