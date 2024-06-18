from itertools import permutations

# Read the input string and integer
S, k = input().split()
k = int(k)

# Generate permutations of size k
perm = sorted(permutations(S, k))

# Print the permutations
for p in perm:
    print("".join(p))
