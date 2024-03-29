# dictionary = a collection of {key:value} pairs ordered and changeable. NO duplicates

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "Germany": "New York",
            "France": "Paris"}

print(capitals.get("USA"))
print(capitals.get("Japan"))

if capitals.get("Japan"):
    print("That capital exists")
else:
    print("That capital doesnt exist")

# update key with new value
capitals.update({"Germany": "Berlin"})
print(capitals)
# you also can insert new key with new value with update method
capitals.update({"Poland": "Warsaw"})
print(capitals)

# printing all keys alone:
keys = capitals.keys()
for key in capitals.keys():
    print(key)

# prinitng all values alone:
values = capitals.values()
for value in capitals.values():
    print(value)

# printing all items (pairs):
items = capitals.items()
for key, value in capitals.items():
    print(f"{key}: {value}")

# removing elements:
capitals.popitem()
print(capitals)
capitals.pop("USA")
print(capitals)
capitals.clear()
print(capitals)
