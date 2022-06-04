#leap year
yr=int(input("enter tbe yr "))
if((yr%4 == 0) and (yr%100 != 0) ):
    print("this is a leap yr")
else:
    print("this not a leap year")    
