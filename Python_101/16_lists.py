numbers = [1, 2, 3, 4]
print(numbers)
print(type(numbers))
tasks = ["make dishes", "play video-games"]
print(tasks, " this list is type--", type(tasks))
print("Using slicing with list: ", tasks[1][5:])

typeslist = [1, True, "hello"]  # Can save different type variables
print(typeslist, " this list is type--", type(typeslist))
print(typeslist[1])

# replace value of list
tasks[0] = "watch platzi courses"
print("replace value of list---", tasks)

print(numbers[1:3])
print(True in typeslist)  # find value in list
