#reverse num
n=int(input("enter the num"))
i=len(str(n))
print("reverse num is")
while(i>0):
    a=n%10
    print(a)
    n=n//10
    
    i=i-1
