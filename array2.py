array1=list(map(int, input("enter the array elements:").split()))
array2=sorted(array1)
print(array2)
sum1=0
for i in array2[:2]:
    sum1+=i
print(sum1)
