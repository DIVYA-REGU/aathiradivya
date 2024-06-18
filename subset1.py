def is_subset(test_cases):
    results = []
    for _ in range(test_cases):
        input()
        set_a = set(map(int, input().split()))
        input()
        set_b = set(map(int, input().split()))
        results.append(set_a.issubset(set_b))
    return results
test_cases = int(input())
results = is_subset(test_cases)
for result in results:
    print("True" if result else "False")
