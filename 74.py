#pornic
n=int(input("enter the no."))
val=0
for i in range(1 , (n//2+1)):
    if(i*(i+1)==n):
        val=1
        break;
if(val==1):
    print("num is pronic")
else:
    print("not a pronic number")
