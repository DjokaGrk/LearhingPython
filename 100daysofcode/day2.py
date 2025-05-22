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
wel = "welcome to the tip calculator"
bill = float(input("koliko je racun "))
tip = float(input("koliko bi hteo da je tip? 10, 12, 15? "))
split = float(input("koliko ljudi deli racun "))

racun = round((bill * tip) / split, 2)
print(f"treba svako od vas dati po {racun}")
