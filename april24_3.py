def is_lower(s1):
    def custom_sort(char):
        if char.islower():
            return (0,char)
        else:
            return (1,char)
    sorted_string=''.join(sorted(s1,key=custom_sort))
    return sorted_string
s2=input()
result=is_lower(s2)
print(result)
