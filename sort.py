num=[10,9,4,4,7,3,2,4]
unique=[]
for n in num:
    if n not in unique:
        unique.append(n)
print("original list: ",num)
print("after removing duplicate: ",unique)
