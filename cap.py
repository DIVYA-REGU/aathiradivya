string = input()
words = string.split()

# Check if there are at least two words in the string
if len(words) >= 2:
    # Capitalize the second word
    words[0]=words[0].capitalize()
    words[1] = words[1].capitalize()

# Join the words back into a string
capitalized_string = ' '.join(words)
print(capitalized_string)  # 
