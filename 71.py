#perfect num
n=int(input("entwr the no"))
sum=0
for i in range(1,n):
   
    if(n%i==0):
    
            
        sum=sum+i
if(sum==n):
    print("%d is perfect" %n)

else:
    print("not a perfect no")
      
           
