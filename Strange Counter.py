# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(raw_input())
total = 0
n = 3
while total < t:
    total += n
    n *= 2
n /= 2
print total - n + (n-t)+1
