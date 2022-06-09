#pronic no. from 1to 10
for n in range(1,100):
    
    val=0
    for i in range(1 , (n//2+1)):
        if(i*(i+1)==n):
            val=1
            break;
    if(val==1):
        print(n)
