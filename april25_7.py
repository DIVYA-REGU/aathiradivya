def countingwords(string):
    words=string.split()
    wordscount={}
    for word in words:
        wordscount[word]=wordscount.get(word,0)+1
    return wordscount
string=input()
result=countingwords(string)
print(result)
