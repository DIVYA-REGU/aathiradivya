n=int(input("enter a number:"))
temp=0
while n>0:
    num=n%10
    temp+=num
    n//=10
print(temp)
