x = 3.3
print(x)
y = 1.1 + 2.2
print(y)
print("-----Transform and comparate in String------")
y_str = format(y, ".2g")
print(y_str)
print(y_str == str(x))
print("-----In Mathematic------")

print("*" * 10)
print(y, x)
tolerance = 0.00001
print(abs(x - y) < tolerance)  # margen-error
