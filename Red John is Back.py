import math

def __isPrime(number):  
    if number <= 1 : return False  
    for i in range(2, int(math.sqrt(number)) + 1):  
        if number % i == 0 :  
            return False  
    return True   

def get_primes(max):
    count=0
    for i in range(2, max + 1):  
        if __isPrime(i): count+=1
    return count

# Enter your code here. Read input from STDIN. Print output to STDOUT
T=int(raw_input())
for i in xrange(T):
    N=int(raw_input())
    D=[0]*(N+1)
    D[0]=1
    for n in xrange(1,N+1):
        if n>=4:
            D[n]=D[n-1]+D[n-4]
        else:
            D[n]=D[n-1]
    print get_primes(D[N])
