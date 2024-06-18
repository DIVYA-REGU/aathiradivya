def custom_sort(char):
    if char.islower():
        return (0, char)  
    elif char.isupper():
        return (1, char)  
    elif char.isdigit():
        if int(char) % 2 == 1:
            return (2, char)  
        else:
            return (3, char)  

def main():
    input_string = input().strip()
    sorted_string = ''.join(sorted(input_string, key=custom_sort))
    print(sorted_string)

if __name__ == "__main__":
    main()
