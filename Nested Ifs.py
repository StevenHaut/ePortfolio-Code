age=int(input("Enter a person's age: "))
if age>0:
    if age<=1:
        person="an infant."
    elif 1<age<13:
        person="a child."
    elif 13<=age<20:
        person="a teenager."
    else:
        person="an adult."
    print("The person is",person)
else:
    print("The person doesn't exist yet. \n"
          "Try again in the future.")
