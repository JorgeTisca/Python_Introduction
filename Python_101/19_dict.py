my_dic = {}
print(type(my_dic))
my_dic = {"plane": "bla bla bla", "name": "Jorge", "last_name": "Tisca", "age": 27}

print(my_dic)
print(len(my_dic))
print(my_dic["age"])
print(my_dic["last_name"])
print(my_dic.get("valor"))  # print value but if not find print None//use prefer get
print("plane" in my_dic)
print("otroqueno" in my_dic)
