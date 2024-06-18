from itertools import combinations_with_replacement
s, k = input().strip().split()
k = int(k)
combs = sorted(combinations_with_replacement(sorted(s), k))
for comb in combs:
    print(''.join(comb))
