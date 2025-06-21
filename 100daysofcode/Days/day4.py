import random

random_broj = random.randint(1, 10)
print(random_broj)

random_broj_0__to_1 = random.random() * 10
print(random_broj_0__to_1)

random_float = random.randint(1, 10)
print(random_float)

head_tails = random.randint(0, 1)
if head_tails == 0:
    print("heads")
else:
    print("tails")


friends = ["djoka", "joka", "ena", "luka"]

# mogucnost 1 da izvuces random iz liste
print(random.choice(friends))

# mogucnost 2
random_friends = random.randint(0, 3)
print(friends[random_friends])

fruits = [
    "Strawberries",
    "Nectarines",
    "Apples",
    "Grapes",
    "Peaches",
    "Cherries",
    "Pears",
]
fruits[-1] = "Melons"
# fruits.append("Lemons")
print(fruits)

fruits = [
    "Strawberries",
    "Nectarines",
    "Apples",
    "Grapes",
    "Peaches",
    "Cherries",
    "Pears",
]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[0][1])
print(dirty_dozen[1][2])
print(dirty_dozen[1][3])
