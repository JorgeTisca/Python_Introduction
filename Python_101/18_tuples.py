numbers = (1, 2, 3, 5)  # tuples init wit()
strings = ("nico", "zule", "santi", "nico")
print(numbers)
print("position 0 = ", numbers[0])
print(type(numbers))

print(strings)

# CRUD
try:
    numbers.append(10)  # Cant add element in Tuple
    print("Add element ", numbers)

except Exception:
    print("Error cant Add element in Tuples")

print(strings)
print("Position of zule--", strings.index("zule"))  # show specific position of world
print("how many nico int tuple---", strings.count("nico"))  # count every world specific

myList = list(strings)  # convert tuple to list
print(myList)
print(type(myList))

myList[1] = "july"
print(myList)

myTuple = tuple(myList)  # convert list to tuple
print(type(myTuple))
