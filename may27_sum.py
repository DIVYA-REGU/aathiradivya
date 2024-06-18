string=input()
vowel=['a','e','i','o','u']
count=0
for i in string:
    if i in vowel:
        count+=1
print(count)
