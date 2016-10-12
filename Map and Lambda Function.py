# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
if N == 0:
    print []
elif N == 1:
    print [0]
else:
    f = [0, 1]
    res = f[:]
    fibonacci = lambda a, b: a + b
    while len(res) < N:
        f += [fibonacci(f[-1], f[-2])]
        res += [pow(f[-1],3)]
    print res
