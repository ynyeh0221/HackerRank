import math
# Enter your code here. Read input from STDIN. Print output to STDOUT
s = raw_input().split(' ')
n = int(s[0])
m = int(s[1])
c = int(s[2])
print math.factorial(n-c + m-c + c -1)
