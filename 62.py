for num in range(1, 1000):
    n=len(str(num))
    no=num

    i=n
    sum=0
    while(i>=1):
   
        a=((num%10)**i)
        sum=sum+a
        num=num//10
        i=i-1
  
    if(sum==no):
        print(no)
           
   
   
