n=int(raw_input())
nums=map(int, raw_input().split())
print all([x>0 for x in nums]) and any([int(str(x)[::-1]) is x for x in nums])
