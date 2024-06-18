arr = list(map(int, input("Enter the array elements: ").split()))
target = 7
arr1 = []
for i in range(len(arr) - 1):
    if arr[i] + arr[i + 1] == target:
        arr1.append((arr[i], arr[i + 1]))
print(arr1)
