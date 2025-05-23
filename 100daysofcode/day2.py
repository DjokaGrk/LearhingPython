# print(type(True))
#
# name = input("enter your name: ")
# print("Number of letters in your name: " + str(len(name)))
#
# print("Number of letters in your name: " + str(len(input("enter your name "))))
# broj = 12345
# string = "string"
# bool = True
# float = 3.14
#
# print(type(broj))
# print(type(string))
# print(type(bool))
# print(type(float))

# print(3 * (3 + 3) / 3 - 3)

# tezina_bmi = float(input("koja je tvoja tezina "))
# visina_bmi = float(input("koja je tvoja visina "))
# bmi = tezina_bmi / (visina_bmi**2)
# print(f"tvoj bmi je {bmi:.2f}")
# print(tezina_bmi, visina_bmi)
# print(f"tvoj bmi je: {tezina_bmi + visina_bmi}")
print("welcome to the tip calculator")
bill = float(input("koliko je racun? $"))
tip = int(input("koliko bi hteo da je tip? 10, 12, 15? "))
total_tip = bill * (tip / 100)
total_bill = bill + total_tip
split = int(input("koliko ljudi deli racun "))

racun = round(total_bill / split, 2)
print(f"treba svako od vas {split} treba dati po {racun} dolara")
