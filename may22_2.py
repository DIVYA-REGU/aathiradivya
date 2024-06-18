arr1=list(map(int,input("enter the first array").split()))
arr2=list(map(int,input("enter the second array").split()))
A=set(arr1)
B=set(arr2)
union_set=A|B
inter_set=A&B
print(union_set)
print(inter_set)
    
