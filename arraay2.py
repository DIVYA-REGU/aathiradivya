n=int(input("enter the number of test cases:"))
for _ in range(n):
    array1 = list(map(int, input("Enter the array elements: ").split()))
    array2 = []

    for i in array1:
        array2.append(i * i)
    print(array2)
