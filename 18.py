s=int(input("enter the selling price"))
c=int(input("engter the cost price"))

p=s-c
l=c-s
if(p<0):
    print("loss")
elif(p==0):
    print("nor loss nor profit")
else:
    print("profit")   
