def fibonacci(n):
    fibsequ=[0,1]
    for i in range(2,n-1):
        fibsequ.append(fibsequ[-1]+fibsequ[-2])
    return fibsequ
n=int(input())
print(fibonacci(n))
        
