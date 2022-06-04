#31
#1st 10 natural no.
for i in range(1,11):
    print(1*i)



#32
#ist 10 natural no. in reverse
i=10
while i>=1:
    print(i*1)
    i=i-1


#33
#1st 10 odd no

for i in range(1,21):
    n=i*1
    if(n%2!=0):
        n=i*1
      
    if(n%2!=0):
        print(i)



#34
#print n natural no
n=int(input("enter the no. to be printed up to"))
for i in range(1,n+1):
    print(1*i)



#35
#reverse n natural no
n= int(input("enter up to white no.s to b eprinted"))

while n >=1:
    print(1*n)
    n=n-1




#36
i=1
sum= int(0)
while i<=3:
    n=int(input("enter the no"))
    sum=sum+n
    i=i+1
print("sum of 3 nos=%d" %sum)
avg=(sum/3)
print("avarage is%d" %avg)



#37
i=1
sum= int(0)
while i<=2:
    n=int(input("enter the no"))
    sum=sum+n
    i=i+1

avg=(sum/2)
print("avarage is%d" %avg)


#38
# sum and avg of 1st n natural no
n=int(input("enter the no. "))
sum=int(0)
for i in range(1,n+1):
  
    sum=sum+i
print(" sum of %d natural no is %d" %(n,sum))
avg=sum/n
print(" average of %d natural no is %d" %(n,avg))
    


#39

#sun of 10 natural no and skip -ve no.
sum=int(0)
for i in range(1,11):
    n=int(input("enter the no. "))
    if(n<0):
        continue;
    else:
         sum=sum+n
  
   
print(" sum of natural no is %d" %sum)

    


#40
#sum of 10 no.s until +ve no. encounters
sum=int(0)
for i in range(1,11):
    n=int(input("enter the no. "))
    if(n>0):
        break;
    else:
         sum=sum+n
  
   
print(" sum of  no.s is %d" %sum)
