#spy num
n=int(input("eneter the num"))
sum=0
mul=1
num=n
i=len(str(n))
while(i>0):
    sum= (n%10)+sum
    mul=(n%10)*mul
    n=n//10
    i=i-1
print("mul =%d \nsum=%d" %(mul,sum))
if(mul==sum):
    print("it is a spy num")
else:
    print("not a spy  num")

