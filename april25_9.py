import re

def split_numbers(s):
    pattern = r'[,.]'  
    return re.split(pattern, s)

def main():
    input_string = input().strip()
    result = split_numbers(input_string)
    for part in result:
        print(part)

if __name__ == "__main__":
    main()
