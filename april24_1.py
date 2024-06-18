def prg(input_string):
    length=len(input_string)
    if length<3:
        print("input is too short")
    else:
        m=length//2
        return input_string[m-1]+input_string[m]+input_string[m+1]
input_string=input()
result=prg(input_string)
print(result)
