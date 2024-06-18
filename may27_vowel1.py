def vowel(string):
    v1='aeiou'
    count=0
    for i in string:
        if i in v1:
            count+=1
    return count
str1=input()
print(vowel(str1))
            
    
