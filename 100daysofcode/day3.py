print("wellcome to rollercoster")
height = int(input("what is your height in cm? "))
age = int(input("koliko imas godina? "))

if height >= 120:
    if age <= 12:
        print("You can ride the rollercoster")
        bill = 7
    elif age <= 18:
        print("You can ride the rollercoster")
        bill = 10
    elif age >= 45 and age <= 55:
        print("You can ride the rollercoster free")
        bill = 0
    else:
        print("You can ride the rollercoster")
        bill = 13

    photo = input("do u wonna photo say y for YES or n for NO: ")
    if photo == "y":
        bill += 3  # dodaje 3 pare za bill
    print(f"Your total bill is {bill} $")
else:
    print("jedi muda nema vozenje")

# print("welcome to EvenOrOdd.py number guesser :)")
#
# num = int(input("upisi broj? "))
#
# if num % 2 == 0:
#     print("number is even")
# else:
#     print("number is odd")

# weight = 85
# height = 1.85
#
# bmi = weight / (height**2)
#
# # 🚨 Do not modify the values above
# # Write your code below 👇
#
# if bmi < 18.5:
#     print("underweight")
# elif bmi < 25:
#     print("normal weight")
# else:
#     print("overweight")

# print("welcome to piza delivery")
# # smallPizza= 15
# # meddiumPizza = 20
# # largePizza = 25
#
# size = input("what size do u wonna take: s, m , l? ")
# pepperoni = input("do u wonna pepperoni? y or n? ")
# cheese = input("do you wonna extra cheese? y or n? ")
# bill = 0
# # pizza size
# if size == "s":
#     bill = 15
#     # pepperoni
#     if pepperoni == "y":
#         bill += 2
# elif size == "m":
#     bill = 20
#     # pepperoni
#     if pepperoni == "y":
#         bill += 3
# elif size == "l":
#     bill = 25
#     # pepperoni
#     if pepperoni == "y":
#         bill += 3
# else:
#     print("nesto ste pogresili")
# # extra cheese
# if cheese == "y":
#     bill += 1
# print(f"your total bill is {bill}$")
