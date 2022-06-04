import math
a=int(input("enter the no a"))
b=int(input("enter the no b"))
c=int(input("enter the no c"))

d=(b*b)-(4*a*c)
if(d<0):
    c1=(-b/(2*a)) -i(math.sqrt(-d))/2*a
    c2=(-b/(2*a)) +i(math.sqrt(-d))/2*a
    print("two distinct complex roots %d and %d"%(c1, c2))
elif(d>0):
    r1=((-b)+ math.sqrt(d))/2*a
    r2=((-b)- math.sqrt(d))/2*a
    print("two distinct real roots %d and %d"%(r1, r2))
elif(d==0):
    r1=r2=-b/(2*a)
    print("2 equal and real real%d and  %d" %(r1,r2))
