# Enter your code here. Read input from STDIN. Print output to STDOUT
N=int(raw_input())
nums=map(int,raw_input().split(" "))
nums=sorted(nums, reverse=True)
for i in xrange(1,len(nums)):
    if nums[i]<nums[0]:
        print nums[i]
        break
