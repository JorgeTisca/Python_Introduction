name = "Jorge"
lastName = "Tiscareño Ponce"
age = 27
print(name)
print(lastName)

fullName = name + " " + lastName
print(fullName)
quote = "I'am Jorge"
print(quote)
quot2 = 'She said " Hello "'
print(quot2)

# Format
template = "Hello Iam " + name + " and my last name is" + lastName
print("V1 ", template)
template = "Hello He is {} and his last name is {}".format(name, lastName)
print(template)

template = f"Hi Iam {name} and my last name {lastName} I am {age} years"
print(template)
