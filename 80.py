#sum of digitd in num
n=int(input("enter the num"))
i=len(str(n))
sum=0

while(i>0):
    a=n%10
    sum=sum+a
    n=n//10
    
    i=i-1
print(sum)
