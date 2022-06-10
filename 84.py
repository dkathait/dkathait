#check whether it is digit alphabet and special charcter
val=input("enter the val") 

if(val>='a'and val<='z') or (val<='A'and val>='z'):
    print("is a alphabet")
elif(val>='0' and val<='9'):
    print("it is digit")
else:
    print("special char")
