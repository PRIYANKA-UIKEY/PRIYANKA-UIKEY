expected_date=int(input("enter the date........"))
expected_month=int(input("enter the month......"))
expected_year=int(input("enter the year......."))
returned_date=int(input("entr the date........."))
returned_month=int(input("enter the month......"))
returned_year=int(input("enter the year.........."))
if returned_date<=expected_date :
    if returned_month<=expected_month:
        if returned_year<=expected_year:
            print("no fine")
        else:
             print("you have  to pay------------",10000 *(returned_year-expected_year))
    else:
        print("you have to pay------------",500*(returned_month-expected_month))
else:
    print("you have to pay------------------",15*(returned_date-expected_date))
    


