def is_palindrome(s):
    s=s.lower()
    return s == s[::-1]
word=input("enter the word:")
if (is_palindrome(word)):
    print("is a palindrome")
else:
    print("not a palindrome")
