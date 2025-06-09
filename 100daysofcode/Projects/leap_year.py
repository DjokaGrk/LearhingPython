def is_leap_year(year):
    if year % 4 != 0:
        return "Year is not leap"
    elif year % 100 != 0:
        return "Year is leap"
    elif year % 400 != 0:
        return "Year is not leap"
    else:
        return "Year is leap"

year = int(input("What year do you want to check? "))
print(is_leap_year(year))