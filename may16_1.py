x, k = map(int, input().split())
polynomial = input().strip()

# Make sure polynomial is evaluated as a string expression with x substituted
result = eval(polynomial)

# Check if the evaluated result matches k
print(result == k)
