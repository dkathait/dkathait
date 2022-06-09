#harshad num
n=(int(input("enter the no of digits to be in digit")))
num=int(input("enter n digit no."))
no=num
sum=0
i=n
while(i>=1):
   
    sum=num%10+sum
  
    num=num//10
    i=i-1
if(no%sum==0):
    print("%d is a harshad no." %no)
else:
    print("%d is not a harshad no." %no)
