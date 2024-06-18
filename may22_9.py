str1=input("enter the string: " )
count={}
for i in str1:
    if i.isalpha():
        if i in count:
            count[i]+=1
        else:
            count[i]=1
for key,value in count.items():
    print(key,"  ocurred",value,"times")
