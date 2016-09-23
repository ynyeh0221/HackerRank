N = int(raw_input())
nums = []
for n in xrange(N):
    nums += [int(raw_input())]
maxx = max(nums)
fibos = [1, 1]
while fibos[-1] < maxx:
    fibos += [fibos[-1] + fibos[-2]]
for n in xrange(N):
    if nums[n] in fibos:
        print "IsFibo"
    else:
        print "IsNotFibo"
