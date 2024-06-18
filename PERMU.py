from itertools import permutations
S, k = input().split()
k = int(k)
perm = sorted(permutations(S, k))
for p in perm:
    print("".join(p))
