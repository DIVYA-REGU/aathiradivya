def splitandjoin(line):
    string=line.split(' ')
    string1='-'.join(string)
    return string1
line=input()
result=splitandjoin(line)
print(result)
