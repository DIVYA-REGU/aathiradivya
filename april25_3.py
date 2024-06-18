def srt_ing(words):
    string=words.split()
    string.sort()
    sorted_sentence=' '.join(string)
    return sorted_sentence
words=input()
result=srt_ing(words)
print(result)
    
    
