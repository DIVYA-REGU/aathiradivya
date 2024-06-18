from itertools import combinations
n = int(input())  
letters = input().split()
k = int(input())
count_a = letters.count('a')
total_combinations = len(list(combinations(letters, k)))
no_a_combinations = len(list(combinations([letter for letter in letters if letter != 'a'], k)))
probability = 1 - (no_a_combinations / total_combinations)
print("{:.4f}".format(probability))
