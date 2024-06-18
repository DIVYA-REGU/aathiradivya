from itertools import groupby
def m(S):
    modified_string=""
    for char, group in groupby(S):
        count=len(list(group))
        modified_string+="("+str(count)+","+char+")"
        return modified_string
S=input()
print(m(S))
        
