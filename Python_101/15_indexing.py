text = "She is expert in Python"
print(text[0])
print(text[1])
# print(text[999]) error for the position
print("-" * 5, "Last letter using length", "-" * 5)
size = len(text)
print("size => ", size)
print(text[size - 1])
print("-" * 5, "Last letter using index", "-" * 5)
# remember the last letter init with position -1, and the first letter with position 0
print(text[-1])

# slicing

print(text[0:5])  # print position 0 to 5

print(text[14:23])  # print position 14 to 23
print(text[:23])  # print init (0) to 23
print(text[10:])  # print position 10 to last position
print(text[:])  # position init to last
print(text[17::2])  # skip 2 or jump every 2 position "Python" --Skip yhn
print(text[::2])  # skip every 2 letters of text
print(text[:13:-1])  # revert the text
