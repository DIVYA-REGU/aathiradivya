def append_string(first,second):
    mid_index=len(first)//2
    first_half=first[:mid_index]
    second_half=first[mid_index:]
    return first_half+second+second_half
first=input()
second=input()
result=append_string(first,second)
print(result)
    

