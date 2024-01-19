is_single = True
print(type(is_single))
is_single = False
print(is_single)
print(not True)  # invert value boolean
is_single = not is_single
print(f"Invert boolean {is_single}")

print("-----More Examples using boolean----")
print(bool(True), bool(False), bool(None))
print(bool(0), bool(-1), bool("house"), bool(24))

print(bool(0.0), bool(0.0j))
print(True + True)
