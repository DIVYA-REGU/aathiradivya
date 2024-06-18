import textwrap
def wraptext(text,width):
    wrappedtext=textwrap.fill(text,width)
    return wrappedtext
text=input()
width=int(input())
wrappedtext=wraptext(text,width)
print(wrappedtext)
