n=int(input("enter a number: "))
temp=n
sum=0
while n>0:
    num=n%10
    fact=1
    for i in range(1,num+1):
        fact*=i
    sum+=fact
    n//=10
if sum==temp:
    print(temp,"is a strong number")
else:
    print(temp,"is not a strong number")
    
