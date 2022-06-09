#neon num
a=int(input("enetr the no"))
num=a**2
n=len(str(num))

sum=0
i=n
while(i>=1):
   
    sum=num%10+sum
  
    num=num//10
    i=i-1
if(a==sum):
    print("%d is a neno no." %a)
else:
    print("%d is not a neon no." %a)
