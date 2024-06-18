if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    x, k = map(int, data[0].split())
    polynomial = data[1]

    # Evaluate the polynomial with x substituted
    result = eval(polynomial)

    # Print True if the result matches k, otherwise False
    print(result == k)
