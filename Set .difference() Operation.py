# Enter your code here. Read input from STDIN. Print output to STDOUT
n1=raw_input()
s1=set(raw_input().split(" "))
n2=raw_input()
s2=set(raw_input().split(" "))
s3=s1.difference(s2)
print len(s3)
