math=int(input("enter the marks"))
chem=int(input("enter the marks"))
phy=int(input("enter the marks"))
eng=int(input("enter the marks"))
hindi=int(input("enter the marks"))
g=((math+chem+phy+eng+hindi)/500)*100
if(g>80):
    print("grade A")
elif(g<40):
    print("grade c")
elif((g>40) and (g<80)):
    print("grade B")
