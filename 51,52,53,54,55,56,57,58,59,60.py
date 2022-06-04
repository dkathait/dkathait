#51
#count the digit in a no
a=int(input("enter the no"))
c=0
while(a>0):
    a=a//10
    c=c+1
print("no. of digit in the no. ", c)




#52
#fibonacci
n=int(input("enter the no up to which series is to be printed"))
a=0
b=1
print("series is")
while(n>0):
    c=a+b
    a=b
    b=c
    print(c)
    n=n-1




#53
# sum of fibonacci
n=int(input("enter the no up to which series is to be printed"))
a=0
b=1
sum=0
print("series is")
while(n>0):
    c=a+b
    a=b
    b=c
    
    sum=sum+c
    n=n-1
print("sum of series is", sum)
    




#54
#factorial of a no
n=int(input("enter the no to find factorial of"))
i=1
print("facters are")
while(i<=n):
    if(n%i==0):
        print(i)
        i=i+1

    



#55
#factorial of a no
n=int(input("enter the no to find factorial of"))
i=1
print("facters are")
while(i<=n):
    if(n%i==0):
        print(i)
        i=i+1

    



#56
#firest digit of the no.
a=int(input("enter the no"))
c=0
while(a>0):
    a=a//10
    if(a>0 and a<10):
         print("first digit is", a)
         break;
         
      
         c=c+1






#57
#last digit of no
n=int(input("enter the no"))
ld=n%10
print("last digit of no is",ld)




#58
#gcd
a=int(input("enter the no"))
b=int(input("enter the no"))
i=1
while(a>=i and b>=i):
    if(a%i==0 and b%i==0):
        gcd=i
    i=i+1
print("gcd is",gcd)
        




















#59






#60
#armstrong
n=int(input("enter the n0"))
sum=0
a=n
while (a>0):
    d=a%10
    sum+= d**3
    a//=10
if n==sum:
    print("armstrong no. is",n)
else:
    print("is not an armstrong no", n)
