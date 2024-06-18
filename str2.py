s=input()
result=[]
for i,char in enumerate(s):
    segment=char.upper()+char.lower()*i
    result.append(segment)
    result1='-'.join(result)
print(result1)
