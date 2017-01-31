number=int(input("Enter a number within the range 1-10: "))
if 1<=number<=10:
    if number==1:
        roman_numeral="I"
    elif number==2:
        roman_numeral="II"
    elif number==3:
        roman_numeral="III"
    elif number==4:
        roman_numeral="IV"
    elif number==5:
        roman_numeral="V"
    elif number==6:
        roman_numeral="VI"
    elif number==7:
        roman_numeral="VII"
    elif number==8:
        roman_numeral="VIII"
    elif number==9:
        roman_numeral="IX"
    else:
        roman_numeral="X"
    print(roman_numeral)
else:
    print("The number you have given is outside the accepted range. \n"
          "Try a number between 1 and 10.")
