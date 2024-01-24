for element in range(1, 20):  # range the for----range(start,finish)
    print(element)

print("-" * 12)
text = "Hola"
for i in text:
    print(i)

print("-" * 12)

my_list = [23, 45, 67, 89, 43]
for i in my_list:
    print(i)
print("-" * 12)

my_tuple = ("nico", "juli", "pedro")

for i in my_tuple:
    print(i)

print("-" * 12)
product = {"name": "Carlos", "color": "Blue", "Age": 27}

for i in product:
    print(i)  # print key
    print(product[i])  # print value
print("-" * 12)
for key, value in product.items():
    print(key, "----", value)
print("-" * 12)
zoo = {
    "Leon": 8,
    "Jirafa": 5,
    "Hipo": 4,
}

for animal, cantidad in zoo.items():
    print(f"En el zoo tenemos el/la {animal} con una poblacion de {cantidad}")

print("-" * 12, "List of Dictionary", "-" * 12)
people = [  # list of dictionary
    {"name": "nico", "age": 34},
    {"name": "zule", "age": 45},
    {"name": "santil", "age": 4},
]

for person in people:
    print(person)

print("-" * 12)
keyPerson = input("Select name or age= ").lower()
for person in people:
    print("name---", person[keyPerson])  # Show specific value
