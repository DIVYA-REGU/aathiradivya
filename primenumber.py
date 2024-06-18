number=int(input("enter the number:"))
if number > 1:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            print(f"{number} is not prime")
            break
    else:
        print(f"{number} is prime")
else:
    print(f"{number} is not prime")
