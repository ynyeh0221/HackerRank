# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in range(int(raw_input())):
    try:
        a, b = map(int, raw_input().split())    
        print(a // b)
    except ZeroDivisionError as e:
        print("Error Code: " + str(e))
    except ValueError as e:
        print("Error Code: " + str(e))
