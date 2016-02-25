import sys,re
if sys.version_info[0]>=3: raw_input=input
for i in range(int(raw_input())):
	try:
		re.compile(raw_input().strip())
		print(True)
	except re.error:
		print(False)
