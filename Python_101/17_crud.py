# CRUD Create, Read, Update & Delete
numbers = [1, 2, 3, 4, 5]
print(numbers[1])
numbers[-1] = 10  # edit the last position
print("Edit last position ", numbers)
numbers.append(700)  # add element
print("Add element ", numbers)

numbers.insert(0, 20)  # add element in specific position
print("Add element in specific position ", numbers)
numbers.insert(3, 25)
print("Add element in specific position ", numbers)

tasks = ["all 1", "all 2", "all 3"]
newList = numbers + tasks  # Fusion list
print("fusion list ", newList)

print("Position od all 2--", newList.index("all 2"))  # find specific position to world
index = newList.index("all 2")
newList[index] = "all change"
print("change position 9---", newList)

newList.remove("all 1")  # remove
print("Delete element all 1---- ", newList)
newList.pop()  # Delete the last element
print("Delete the last number---", newList)

newList.pop(2)  # Delete the position specific
print("Delet specific position (2)---", newList)

newList.reverse()  # invert list
print("invert list---", newList)

numbers.sort()  # order numbers
print("Order numbers---", numbers)

strings = ["re", "ab", "ed"]
strings.sort()
print("Order string---", strings)
