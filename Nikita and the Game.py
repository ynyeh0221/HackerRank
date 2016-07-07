# recursive, time out for testcase 7, 8, 9, 10

# Enter your code here. Read input from STDIN. Print output to STDOUT
def helper(num):
    if len(num) == 1:
        return 0
    has_ans = False
    for i in xrange(len(num)):
        if num[:i] and num[i:] and sum(num[:i]) == sum(num[i:]):
            has_ans = True
            return max(helper(num[:i]), helper(num[i:])) + 1
    if has_ans == False:
        return 0
            
T = int(raw_input())
for t in xrange(T):
    n = int(raw_input())
    num = map(int, raw_input().split(' '))
    if all(v == 0 for v in num):
        print n-1
    else:
        print helper(num)
