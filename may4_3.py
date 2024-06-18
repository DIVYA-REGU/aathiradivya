def fact(num):
    for i in range(num):
        f=1
        f=i*fact
        i=i+i
        return fact
num-int(input())
print(fact(num))
