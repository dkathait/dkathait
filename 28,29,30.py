#28
pa=int(input("enter the principle value"))
ri=int(input("enter the rate of interest"))
yr=int(input("enter the yrs"))

si=(pa*ri*yr)/100
print("%d is the  simlpe interest" %si)



#29
i=1
sum= int(0)
while i<=10:
    n=int(input("enter the no"))
    sum=sum+n
    i=i+1
print("sum of 10 nos=%d" %sum)
avg=(sum/10)
print("avarage is%d" %avg)




#30
#1st 10 even no.
for i in range(1, 11):
    print(i*2)
     
