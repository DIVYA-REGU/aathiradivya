array = [1, 2, 3, 1, 2,5,1]
element_count = {} # Dictionary to store the count of each element

# Count occurrences of each element
for i in array:
    if i in element_count:
        element_count[i] += 1
    else:
        element_count[i] = 1

# Print the count for each unique element
for key, value in element_count.items():
    if value%2!=0:
        print(key,"occured odd times")
    
    
