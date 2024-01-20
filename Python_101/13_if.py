if True:
    print("If True")

if False:
    print("Never show")

pet = input("What are you favorite pet: ")

if pet == "dog":
    print("Congratulations you have good luck")
elif pet == "cat":
    print("Tsssss")
elif pet == "fish":
    print("You are the best")
else:
    print("Don´t have pet interesting")


stock = int(input("Write Stock: "))
if stock >= 100 and stock <= 1000:
    print("Correct Stock")
else:
    print("Incorrect Stock")

# Pair or InPair
print("----Pair or InPair----")
num = int(input("Write number: "))
if num % 2 == 0:
    print("Is pair")
else:
    print("Is pair")
