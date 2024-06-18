num=[41,23,21,2,34,21]
largest=smallest=num[0]
for n in num:
    if n>largest:
        largest=n
        print(largest)
    elif n<smallest:
        smallest=n
        print(smallest)
print("largest: ",largest)
print("smallest: ",smallest)


