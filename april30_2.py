words=input()
count=0
count1=0
for word in words:
    if word in "aeiou":
        count +=1
    elif word.isalpha():
        count1 +=1
        
print("vowels: ",count)
print("consonants :",count1)
