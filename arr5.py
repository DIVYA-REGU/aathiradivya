def smallest(arr):
    small=arr[0]
    for i in arr:
        if i<small:
            small=i
    return small
n=[34,23,1,5]
print(smallest(n))
    
