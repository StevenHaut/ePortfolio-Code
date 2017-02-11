number_of_days = int(input("Enter the number of days: "))
salary = 0
pennies = 0.01

for days in range(1, number_of_days + 1):
    salary += pennies
    pennies *= 2
    print("Your salary on day", days, "is $", format(salary, ',.2f'))
