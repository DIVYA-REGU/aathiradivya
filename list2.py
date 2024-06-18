def f(n, arr):
    u= sorted(set(arr), reverse=True)
    if len(u) > 1:
        r1 = u[1]
        return r1
    else:
        return "There is no runner-up score."
n = int(input())
arr = list(map(int, input().split()))
r2 = f(n,arr)
print("The runner-up score is:", r2)
