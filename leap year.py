year=int(input("enter the number"))
if year%100==0:
    if year%400==0:
        print("leap year")
    else:
        print("not leap year")
else:
    if year%4==0:
        print("leap year")
    else: 
        print("not leap year")