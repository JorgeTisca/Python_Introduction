text = "She is developer Python "
print("JavaScript" in text)  # find the world and return True or False
print("Python" in text)
"""''
if "Python" in text:
    print("Correct")
else:
    print("Incorrect")

""" ""
size = len("love  ")  # how many caracter you have in text
print(size)

print(text, text.upper())
print(text.lower())

print(text.count("a"))  # Count times use the world or letter
print(text.swapcase())  # change the upper and lower  for invert
print(text.startswith("She"))  # show if tect init for specific world
print(text.endswith("Java"))  # show if tect init for specific world
print(text.replace("Python", "Flutter"))  # change specific world

text2 = "this is Title"
print(text2)
print(text2.capitalize())  # upercase just the fist world
print(text2.title())  # cahnge uppercase the first letter every world
print(text2.isdigit())  # show if world is digit
print("398".isdigit())
