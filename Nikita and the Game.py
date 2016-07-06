# recursive, time out for testcase 7, 8, 9, 10

# Enter your code here. Read input from STDIN. Print output to STDOUT
def helper(num):
    if len(num) == 1:
        return 0
    flag = 0
    for i in xrange(len(num)):
        if num[:i] and num[i:] and sum(num[:i]) == sum(num[i:]):
            flag = 1
            return max(helper(num[:i]), helper(num[i:])) + 1
    if flag == 0:
        return 0
            
T = int(raw_input())
for t in xrange(T):
    n = int(raw_input())
    num = map(int, raw_input().split(' '))
    if all(v == 0 for v in num):
        print n-1
    else:
        print helper(num)
