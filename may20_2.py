str1=input()
character='aeiou'
count=0
for char in str1:
    if char in character:
        count=count+1
print("number of vowels",count)
