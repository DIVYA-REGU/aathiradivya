from itertools import product
A = list(map(int, input().split()))
B = list(map(int, input().split()))
cartesian_product = list(product(A, B))
print(" ".join([f"({x},{y})" for x, y in cartesian_product]))
