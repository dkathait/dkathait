#strong
n=int(input("enter the num"))
num=n
i=len(str(n))

while(i>0):
    a=n%10
    i=1
    sum=0
    while(a<=i):
        if(a%i==0):
            sum=sum+a
            
            
            i=i+1
    n=n//10
    
    i=i-1
if(sum==num):
    print("no is strong")
else:
    print("not a strong num")

