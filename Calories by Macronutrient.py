# Create a global variable.
total_cal = 0


# Defines the function "main".
def main():
    # Asks the user for grams of fat consumed in a day.
    # The variable "fat_grams" is assigned the entered value and then passed to the "calc_fat_grams" function.
    fat_grams = float(input("Enter the number of fat grams consumed in a day: "))
    # Asks the user for grams of carbohydrates consumed in a day.
    # The variable "carb_grams" is assigned the entered value and then passed to the "calc_carb_grams" function.
    carb_grams = float(input("Enter the number of carbohydrate grams consumed in a day: "))
    # Asks the user for grams of protein consumed in a day.
    # The variable "protein_grams" is assigned the entered value and then passed to the "calc_protein_grams" function.
    protein_grams = float(input("Enter the number of protein grams consumed in a day: "))
    # The variable "fat_cal" is assigned the return value from the function "calc_fat_cal".
    # Calls the "calc_fat_cal" function, passed with the argument "fat_grams".
    fat_cal = calc_fat_cal(fat_grams)
    # The variable "carb_cal" is assigned the return value from the function "calc_carb_cal".
    # Calls the "calc_carb_cal" function, passed with the argument "carb_grams".
    carb_cal = calc_carb_cal(carb_grams)
    # The variable "protein_cal" is assigned the return value from the function "calc_protein_cal".
    # Calls the "calc_protein_cal" function, passed with the argument "protein_grams".
    protein_cal = calc_protein_cal(protein_grams)
    # Calls the "calc_total_cal" function, passed with the three arguments "fat_grams", "carb_cal", and "protein_cal".
    calc_total_cal(fat_cal, carb_cal, protein_cal)
    # Calls the "print_total_cal" function.
    print_total_cal()


# Defines the function "calc_fat_cal" with the parameter "fg".
def calc_fat_cal(fg):
    # The variable "cal_fat" is assigned the calculated float value
    # of the parameter "fg", which is accepted as "fat_grams", multiplied by 9.
    cal_fat = float(fg*9)
    # Prints the fat calories, to one decimal place, on the screen, using "cal_fat".
    print("There are " + format(cal_fat, ',.1f') + " calories from fat.")
    # Returns the variable "cal_fat" to the called function, which is assigned to the variable "fat_cal".
    return cal_fat


# Defines the function "cal_carb_cal" with the parameter "cg".
def calc_carb_cal(cg):
    # The variable "cal_carb" is assigned the calculated float value
    # of the parameter "cg", which is accepted as "carb_grams", multiplied by 4.
    cal_carb = float(cg*4)
    # Prints the carbohydrate calories, to one decimal place, on the screen, using "cal_carb".
    print("There are " + format(cal_carb, ',.1f') + " calories from carbohydrates.")
    # Returns the variable "cal_carb" to the called function, which is assigned to the variable "carb_cal".
    return cal_carb


# Defines the function "calc_protein_cal" with the parameter "pg".
def calc_protein_cal(pg):
    # The variable "cal_protein" is assigned the calculated float value
    # of the parameter "pg", which is accepted as "protein_grams", multiplied by 4.
    cal_protein = float(pg*4)
    # Prints the carbohydrate calories, to one decimal place, on the screen, using "cal_protein".
    print("There are " + format(cal_protein, ',.1f') + " calories from protein.")
    # Returns the variable "cal_protein" to the called function, which is assigned to the variable "protein_cal".
    return cal_protein


# Defines the function "calc_total_cal" with the parameters "fat_cal", "carb_cal", and "protein_cal".
def calc_total_cal(fat_cal, carb_cal, protein_cal):
    # Calls the global variable "total_cal".
    global total_cal
    # Redefines the global variable "total_cal" as the sum of "fat_cal", "carb_cal" and "protein_cal".
    total_cal = fat_cal + carb_cal + protein_cal


# Defines the function "print_total_cal".
def print_total_cal():
    # Prints the total daily calories, to one decimal place, on the screen, using the global variable "total_cal".
    print("There are " + format(total_cal, ',.1f') + " total calories for the day.")
# Calls the function "main".
main()
