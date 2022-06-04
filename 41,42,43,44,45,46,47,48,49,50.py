#41
#electricity bill
u=int(input("enter the unit consumed"))
if(u<=100):
    pay=100*1.5
    fa=25
elif(u<=200):
    pay=(100)*2.5+(u-100)*2.5
    fa=50
elif(u<=300):
    pay=(100)*2.5+(100)*2.5+(u-200)*4
    fa=75
else:
    pay=0
    fa=1500
total=pay+fa
print("total bill =%d" %total)




#42
#distance b/w tow points
import math
x1=int(input("enter 1st coordinate of  1st point  "))
x2=int(input("enter 2st coordinate of  1st point  "))
y1=int(input("enter 1st coordinate of  2st point  "))
y2=int(input("enter 2st coordinate of  2st point  "))
a=(x2-x1)*(x2-x1)+(y2-y1)^(y2-y1)
dis=math.sqrt(a)
print("distance of 2 points is %d"%dis)



#43
# average  and % of marks
i=1
sum= int(0)
while i<=5:
    n=int(input("enter the marks"))
    sum=sum+n
    i=i+1

avg=(sum/5)
print("avarage is%d" %avg)
per=(sum/500)*100
print("%d is the persent" %per)






#44
#print data and time
from datetime import datetime
c=datetime.now()
print("the cureent data and time is ",c)



#45
#sun to natural no.s
n=int(input("enter  no. upto what sun is to be found "))
sum=int(0)
for i in range(1,n+1):
    a=int(input("enter the no. "))
  
    sum=sum+a
print(" sum of %d natural no is %d" %(n,sum))

    




#46
n=int(input("enter the no. to be printed up to"))
sum=int(0)
for i in range(1,n+1):
    a=i*2
    sum=sum+a
print("sum of n natural nos is " ,sum)




#47
#sum and average od natural no
a=int(input("enter total no"))
i=1
sum= int(0)
while i<=a:
    n=int(input("enter the no"))
    sum=sum+n
    i=i+1
print("sum of n nos=%d" %sum)
avg=(sum/a)
print("avarage is%d" %avg)





#48
#sum of odd no
sum=int(0)
for i in range(1,21):
    n=i*1
    if(n%2!=0):
        a=i
    sum=sum+a
print("sum is", a)





#49
#sum od even and odd no.s
sum=int(0)
for i in range(1,21):
    n=i*1
    if(n%2!=0):
        a=i
    sumo=sum+a
for i in range(1, 11):
    p=i*2
    sume=sum+p
tsum=sumo+sume
print("sum of 1st even and odd nos is ", tsum)

     



#50
#arithmetic op.s using function

def arithmetic (a,b,c):
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

arithmetic(8,4,10)
