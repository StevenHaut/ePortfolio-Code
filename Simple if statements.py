number=int(input("Enter a number between 1-7: "))
if 1<=number<=7:
    if number==1:
        day_of_week="Monday"
    elif number==2:
        day_of_week="Tuesday"
    elif number==3:
        day_of_week="Wednesday"
    elif number==4:
        day_of_week="Thursday"
    elif number==5:
        day_of_week="Friday"
    elif number==6:
        day_of_week="Saturday"
    else:
        day_of_week="Sunday"
    print("The day is", day_of_week)
else:
    print("The number you have given is outside the accepted range. \n"
          "Try a number between 1 and 7.")
