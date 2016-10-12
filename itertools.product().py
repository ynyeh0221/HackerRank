import itertools
A = map(int, raw_input().split())
B = map(int, raw_input().split())
print ' '.join(str(e) for e in list(itertools.product(A, B)))
