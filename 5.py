#arithmetic
a=int(input("enter no"))
b=int(input("entwr 2nd no"))
op=str(input("operation x(+),z(*),y(-)"))
if(op=='x'):
    sum=a+b
    print(sum)
elif(op=='y'):
    sub=a-b  
    print(sub)  
elif(op=='z'):
    mul=a*b
    print(mul)
