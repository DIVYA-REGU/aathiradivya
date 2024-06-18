import math
test_cases=int(input("enter the number of test cases:"))
for i in range(test_cases):
    n=int(input("enter the number:"))
    squareroot=math.sqrt(n)
    if squareroot.is_integer():
        print("true")
    else:
        print("false")
