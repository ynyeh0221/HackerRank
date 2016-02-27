import sys,numpy
if sys.version_info[0]>=3: raw_input=input
n,m=map(int,raw_input().split())
num=[]
for _ in range(n):
	num.append([int(i) for i in raw_input().split()])
num=numpy.array(num)
print(numpy.transpose(num))
print(num.flatten())
