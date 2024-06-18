from itertools import combinations
def print_combinations(S,k):
    for size in range(1,k+1):
        for combo in combinations(sorted(S),size):
            print(''.join(combo))
S,k=input().split()
k=int(k)
print_combinations(S,k)
