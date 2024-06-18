original_string=input()
characters_to_remove=",.!"
modified_string=""
for char in original_string:
    if char not in characters_to_remove:
        modified_string+=char
print(modified_string)
