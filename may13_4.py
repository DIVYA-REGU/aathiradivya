n=int(input("enter the number: "))
if n==1:
    print(n,"is not a prime number")
for i in range(2,n):
    if n%i==0:
        print(n,"is not a prime number")
    else:
        print(n,"is a prime number")