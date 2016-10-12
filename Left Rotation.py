[n,d] = map(int, raw_input().split())
a = map(int, raw_input().split())
d %= n
print ' '.join(str(e) for e in (a[d:] + a[:d]))
