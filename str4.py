def check_string(s):
    if any(c.isalnum() for c in s):
        print("True")
    else:
        print("False")
    if any(c.isalpha() for c in s):
        print("True")
    else:
        print("False")
    if any(c.isdigit() for c in s):
        print("True")
    else:
        print("False")
    if any(c.isupper() for c in s):
        print("True")
    else:
        print("False")
    if any(c.islower() for c in s):
        print("True")
    else:
        print("False")
input_string = input()
check_string(input_string)
