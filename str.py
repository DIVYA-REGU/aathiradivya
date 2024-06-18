def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i:i+len(sub_string)] == sub_string:
            count += 1
    return count

# Input
original_string = input()
substring = input()

# Output
print(count_substring(original_string, substring))
