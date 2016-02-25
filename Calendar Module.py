# Enter your code here. Read input from STDIN. Print output to STDOUT
import time
from datetime import date
week=["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
da=map(int, raw_input().split(" "))
print week[date(da[2], da[0], da[1]).weekday()]
