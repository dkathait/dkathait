#disrium no.
n=(int(input("enter the no of digits to b e in digit")))
num=int(input("enter n digit no."))
no=num

i=n
sum=0
while(i>=1):
   
    a=((num%10)**i)
    sum=sum+a
    num=num//10
    i=i-1
print(sum)
if(sum==no):
    print("%d is disarium no." %no)
else:
    print("%d is not a disarium no." %n0)
   
   
