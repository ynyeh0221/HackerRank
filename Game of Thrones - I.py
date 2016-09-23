string = raw_input()
 
found = False
# Write the code to find the required palindrome and then assign the variable 'found' a value of True or False

freq = {}
for i in string:
    if i not in freq:
        freq[i] = 0
    freq[i] += 1
oddfreq = 0
for i in freq:
    if freq[i] % 2 != 0:
        oddfreq += 1
if oddfreq <= 1:
    found = True

if not found:
    print("NO")
else:
    print("YES")
