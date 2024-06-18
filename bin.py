def print_formatted(number):
    width = len(bin(number)[2:])  # Calculate width based on binary representation
    for i in range(1, number + 1):
        decimal = str(i)
        octal = oct(i)[2:]
        hexadecimal = hex(i)[2:].upper()
        binary = bin(i)[2:]
        print(f"{decimal:>{width}} {octal:>{width}} {hexadecimal:>{width}} {binary:>{width}}")

# Get input from the user
number = int(input())

# Call the function with user input
print_formatted(number)
