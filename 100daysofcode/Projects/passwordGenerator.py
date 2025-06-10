import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "@", "#", "$", "%", "^",
           "&", "*", "(", ")", "-", "_", "=", "+"]
# nesumicna_slova = []
# nesumicni_simboli = []
# nesumicni_brojevi = []
print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
# if nr_letters <= len(letters):
#     nesumicna_slova = random.sample(letters, nr_letters)
#     # print("Letters:", nesumicna_slova)
#     #
# if nr_symbols <= len(symbols):
#     nesumicni_simboli = random.sample(symbols, nr_symbols)
#     # print("Symbols:", nesumicni_simboli)
#     #
# if nr_numbers <= len(numbers):
#     nesumicni_brojevi = random.sample(numbers, nr_numbers)
#     # print("Numbers:", nesumicni_brojevi)
# password_list = nesumicna_slova + nesumicni_simboli + nesumicni_brojevi
# password_weak = "".join(password_list)
# random.shuffle(password_list)
# # print("Password list:", str(password_list))
# password = "".join(password_list)
# print(f"Your weak password is: {password_weak}")
# print(f"Your strong password is: {password}")
#
# easy lvl password generator
# password = ""
# for char in range(0, nr_letters):
#     password += random.choice(letters)
# for char in range(0, nr_symbols):
#     password += random.choice(symbols)
# for char in range(0, nr_numbers):
#     password += random.choice(numbers)
# print(f"Your weak password is: {password_list}")

# hard lvl password generator
password_list = []
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))
for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))
for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))
# print(f"Your weak password is: {password_list}")
random.shuffle(password_list)
# print(password_list)
password = ""
for char in password_list:
    password += char
# print(f"Your strong password is: {password}")
str_password = "".join(password_list)
print(f"Your password is: {str_password}")