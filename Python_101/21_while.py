counter = 0

while counter < 10:
    counter += 1
    print(counter)
print("-" * 10)
counter = 0
while counter < 20:
    counter += 1

    print(counter)
    if counter == 15:
        print("Finis for break")
        break  # break While

print("-" * 10)
counter = 0
while counter < 20:
    counter += 1

    if counter <= 15:
        print(counter)
        continue  # Continue next and skip before instructions
    print("Using continue ", counter)
