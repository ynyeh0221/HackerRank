# Enter your code here. Read input from STDIN. Print output to STDOUT
N=int(raw_input())
students = [[0 for x in range(2)] for x in range(N)]
nums=[0]*N
for i in xrange(N):
    students[i][0]=raw_input()
    students[i][1]=float(raw_input())
    nums[i]=students[i][1]
students=sorted(students, key=lambda x:(x[1],x[0]))
nums=sorted(nums)
second=0
for i in xrange(1,len(nums)):
    if nums[i]>nums[0]:
        second=nums[i]
        break
for i in xrange(N):
    if students[i][1]==second:
        print students[i][0]
