# Enter your code here. Read input from STDIN. Print output to STDOUT
def insertionSort(ar):
    shift = 0
    for i in xrange(1, len(ar)):
        temp = ar[i]
        j = i
        while j > 0 and temp < ar[j-1]:
            ar[j] = ar[j-1]
            j -= 1
            shift += 1
        ar[j] = temp
    print shift

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
