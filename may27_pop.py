n=float(input("enter the population: "))
total=n
count=0
while total<1200:
    total=total*1.02+50
    count+=1
print("population will reach",total,"in",count,"years")

