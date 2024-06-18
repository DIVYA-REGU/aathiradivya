def sum_of_ele(array):
    array2=sorted(array)
    sum1=0
    for i in array2[:2]:
        sum1+=i
    return sum1
array=list(map(int,input().split()))
print(sum_of_ele(array))
