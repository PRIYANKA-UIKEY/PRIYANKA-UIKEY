print("WELCOME TO STATE BANK OF INDIA")
print("swipe your card here")
language=(input("enter the language..."))
if language=="english":   
    transaction=["balance enqary","withdarw money","diposit","tranfer money","quite"]
    pin=(input("enter your pin to number..."))
    amount=200000
    if pin==pin:
        if len(pin)==4:
           print("1 choose your transacation")
           print("2 balance enquiry")
           print("3 withdarw money")
           print("4 diposit")
           print("5 tranfer money")
           print("6 queit")
           trans=input(" transacation...")
           if trans=="balance enquiry":
               swipe=input("do you want enquiry your money?',,,,,,,")
               if swipe=="yes":
                   print(amount,"is your money,thanks for using state of india")
               else:
                    print("nothing")
           elif trans=="withdra money":
               amount1=int(input("enter your amount to proceed"))
               if amount1>=0 and amount1<=200000:
                   print("collect your cash",amount-amount1,"is left in your account.thanks for using SBI BANK")
               else:
                   print("enter vaild amount to proceed")
           elif trans=="diposit":
               amount2=int(input("enter the amount to deposit=")) 
               if amount2>=1:
                   print("your diposit is done sucsessfully !now you have",amount+amount2,"thanks for using SBI india" ) 
               else:
                   print("enter vaild amount to diposit=")   
           elif trans=="tranfer money":
                transfer_money=int(input("enter your amount tranfer")) 
                if transfer_money>=0:
                    print("your money has been tranfered !",amount-transfer_money," is left in your account, thanks for using SBI bank")
                else:
                    print("enter valid amount") 
           elif trans=="queit":
               quite=input("press to queit") 
               if quite=="yes":
                   print("queit") 
               else:
                   print("choose any transacation please")
           else:
               print("your password is not valid ,try again") 
        else:
            print("your passward is wrong")  
    else:
        print("sorry we dont have that language")
else:
    print("thanks for using SBI bank")                   


    

