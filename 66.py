#1 to 100 harshad num



for num in range(1, 200):
    n=len(str(num))
    no=num
    i=n
    
    sum=0
    while(i>=1):
   
       
        sum=sum+num%10
      
        num=num//10
        i=i-1
       
    if(no%sum==0):
            print(no)
        
