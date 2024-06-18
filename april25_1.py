original_string=input()
res = ''.join(filter(lambda i: i.isdigit(),original_string))
print(res)
