number_of_years = int(input("Enter the number of years: "))
total_rainfall = 0
total_months = 0

for years in range(1, number_of_years + 1):
    for months in range(1, 13):
        if months == 1:
            months = "January"
        elif months == 2:
            months = "February"
        elif months == 3:
            months = "March"
        elif months == 4:
            months = "April"
        elif months == 5:
            months = "May"
        elif months == 6:
            months = "June"
        elif months == 7:
            months = "July"
        elif months == 8:
            months = "August"
        elif months == 9:
            months = "September"
        elif months == 10:
            months = "October"
        elif months == 11:
            months = "November"
        else:
            months = "December"
        print("Enter the inches of rainfall in", months, "of year", years)
        inches_of_rainfall = float(input())
        total_rainfall += inches_of_rainfall
        total_months += 1
        average_rainfall = total_rainfall/total_months
        print("The total amount of rainfall for", total_months, "months is", format(total_rainfall, ',.2f'), "inches")
        print("The average amount of rainfall for", total_months, "months is", format(average_rainfall, ',.2f'), "inches per month")
