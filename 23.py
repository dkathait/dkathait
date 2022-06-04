n=int(input("enter the no"))
if((n%5==0) and (n%11==0)):
    print("%d is divisible by both 11 & 5" %n)
elif((n%5==0) and (n%11!=0)):
    print("%d is divisible by 5 not with 11" %n)
elif((n%5!=0) and (n%11==0)):
      print("%d is divisible by 11 not with 5" %n)
