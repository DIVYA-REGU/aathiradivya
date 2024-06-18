import re
str1=input("enter the uid number: ")
count1=0
count2=0
if not re.match("^[a-zA-Z0-9]*$", str1):
    print("invalid")
for i in str1:
    if i.isupper():
        count1+=1
for j in str1:
    if j.isdigit():
        count2+=1
total=count1+count2
if total==10:
    print("valid")
else:
    print("invalid")
    
    
