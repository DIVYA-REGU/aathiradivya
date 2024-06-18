def count_distinct_stamps(N):
    stamps_set=set()
    for _ in range(N):
        stamp=input().strip()
        stamps_set.add(stamp)
    return len(stamps_set)
N=int(input())
print(count_distinct_stamps(N))
        
