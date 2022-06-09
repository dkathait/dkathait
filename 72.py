#prime no.
n=int(input("enter thre no"))
i=2
while(i<=n):
    if(n%i==0):
        print("%d is not a prime no."%n)
        break;
        i=i+1
    else:
        print("%is a prime no."%n)
        break;

