from itertools import product
A = list(map(int, input().split()))
B = list(map(int, input().split()))
cartesian_product = list(product(A, B))
for item in cartesian_product:
    print(item, end=" ")
