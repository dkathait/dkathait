#prime factors
n=int(input("enter the num"))
for i in range(2, n+1):
    if(n%i==0):
        p=1
        for j in range(2,(i//2+1)):
            if(i%j==0):
                p=0
                break;
        if(p==1):
            print(i)
