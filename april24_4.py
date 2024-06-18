def counting(s1):
    countone=0
    counttwo=0
    countthree=0
    for char in s1:
        if char.isalpha():
            countone+=1
        elif char.isdigit():
            counttwo+=1
        else:
            countthree+=1
    return countone,counttwo,countthree
s1=input()
letters,digit,special_char=counting(s1)
print("letters: ",letters)
print("digits: ",digit)
print("special charaters: ",special_char)
































            
            
