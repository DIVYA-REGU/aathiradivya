import re
def find_substrings_with_vowels(s):
    vowels = 'aeiouAEIOU'
    consonants = 'qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM'
    pattern = re.compile(r'(?<=[' + consonants + '])([' + vowels + ']{2,})(?=[' + consonants + '])')
    substrings = pattern.findall(s)
    return substrings if substrings else -1
s = input().strip()
result = find_substrings_with_vowels(s)
if result != -1:
    for substring in result:
        print(substring)
else:
    print(-1)
