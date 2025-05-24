print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

prepraka1 = input("ides li levo ili desno?\n").lower()
izgubio = "izgubio si"

if prepraka1 == "levo":
    prepreka2 = input("cekas li ili plivas?\n").lower()
    if prepreka2 == "cekam":
        prepreka3 = input("izaberi kutiju: crvena , plava ili zuta?\n").lower()
        if prepreka3 == "zuta":
            print("pobedio si!")
        elif prepreka3 == "crvenu":
            print(izgubio)
        else:
            print(izgubio)

    else:
        print(izgubio)
else:
    print(izgubio)
