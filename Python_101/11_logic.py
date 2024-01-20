# AND
print("-----AND-----")
print("True and True=", True and True)
print("True and False=", True and False)
print("False and True=", False and True)
print("False and False=", False and False)

print(10 > 5 and 5 < 10)
print(10 > 5 and 5 > 10)
validation = True
try:
    stock = int(input("Write Stock: "))
    print(stock)
    print(stock >= 100 and stock <= 1000)
except ValueError:
    print("Error dont write number ")


# OR
print("-----OR-----")
print("True or True= ", True or True)
print("True or False= ", True or False)
print("False or True= ", False or True)
print("False or False= ", False or False)
try:
    role = str(input("Write rol: "))
    print(role)
    print(role == "admin" and role == "seller")
except ValueError:
    print("Error ")
