n=int(input("enter a number:"))
for i in range(1,int(n**0.5)+1):
    if (n%i==0):
        print(i)
