list1=list(map(int,input().split()))
n=len(list1)
sum1=0
average=0
for i in list1:
    sum1+=i
average=sum1/n
print(average)
