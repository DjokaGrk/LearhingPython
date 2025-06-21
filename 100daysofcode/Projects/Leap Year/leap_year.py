def is_leap_year(year):
    """
    Returns whether the given year is a leap year.
    """
    if year < 0:
        return "Year cannot be negative"
    if year % 4 != 0:
        return "Year is not leap"
    elif year % 100 != 0:
        return "Year is leap"
    elif year % 400 != 0:
        return "Year is not leap"
    else:
        return "Year is leap"

while True:
    year = int(input("What year do you want to check? "))
    print(is_leap_year(year))
    again = input("Type 'y' if you want to check another year, or any other key to exit: ").lower()
    if again != 'y':
        print("Exiting the program")
        break
