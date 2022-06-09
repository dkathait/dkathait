#1 to 100 palindrome no.
for num in range(1, 200):
   
    n=num
    nnum=0
    while(n>0):
   
        nnum=nnum*10+n%10
        n=n//10
    if(nnum==num):
        print(num)
   
