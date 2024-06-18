def p(n):
    
    for i in range(1,n+1):
       outputs = ""
       for j in range(0,i):
           outputs=outputs+"*"
       print(outputs)
       
n=5
p(n)
