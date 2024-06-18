def swap_cases(string):
    return string.swapcase()

if __name__ == "__main__":
    input_string = input("Enter the string: ")
    swapped_string = swap_cases(input_string)
    print("Swapped string:", swapped_string)
