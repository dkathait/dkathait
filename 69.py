#palindrome
num=int(input("ener the no"))
n=num
nnum=0
while(n>0):
   
    nnum=nnum*10+n%10
    n=n//10
print(nnum)
if(nnum==num):
    print("%d is a palindrome no" %num)
else:
    print("not a palindrome no.")
