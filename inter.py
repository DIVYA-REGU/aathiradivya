word_counts = {}
for _ in range(n):
    word = input().strip()
    word_counts[word] = word_counts.get(word, 0) + 1
print(len(word_counts))
print(*word_counts.values())
