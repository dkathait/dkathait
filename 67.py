import math
n=(int(input("enter the no of digits to be in digit")))
num=int(input("enter n digit no."))
no=num
sum=0
i=n
while(i>=1):
   
    sum=math.factorial(num%10)+sum
  
    num=num//10
    i=i-1
print(sum)
if(sum==no):
    print("%d is krishnamurthy no." %no)
else:
    print("%d is not a krishnamurthy no." %no)
   
   
