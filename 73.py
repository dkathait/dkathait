for n in range(1,10):
    i=2
    while(i<=n):
        if(n%i==0):
            print("%d is not a prime no."%n)
            i=i+1
            break;
           
        else:
            print("%is a prime no."%n)
            break;
