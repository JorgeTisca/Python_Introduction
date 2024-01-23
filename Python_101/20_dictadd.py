person = {
    "name": "jorge",
    "last_name": "Tiscareño",
    "langs": ["python", "javascript"],
    "age": 99,
}
print(person)
# ADD ELEMENTS
print("-" * 3, "ADD ELEMENTS", "-" * 3)
person["good"] = "Hello"
print(person)
# UPDATE ELEMENTS
print("-" * 3, "UPDATE ELEMENTS", "-" * 3)
person["name"] = "Alejandro"
person["age"] -= 50
person["langs"].append("rust")
print(person)

# DELETE ELEMENT
del person["last_name"]  # Used "del" for delete
print("Delete last name: ", person)
person.pop("age")  # Used "pop"
print("Delete Age: ", person)

# ITEMS--- Show Dictionary in tuples
print("---ITEMS---")
print(person.items())
# KEYS--- Show Dictionary in list just keys
print("---KEYS---")
print(person.keys())
# VALUE--
print("---VALUES---")
print(person.values())
