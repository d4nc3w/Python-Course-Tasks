
fruits = ["apple", "banana", "cherry", "orange"]
vegetables = ["carrot", "potatoes"]
meats = ["chicken", "fish", "turkey"]

# creating 2d collection from lists
grocieres = [fruits, vegetables, meats]
print(grocieres)
print()

# correct way to display collections in 2d:
for collection in grocieres:
    print(collection)
# iterate over every element in 2d collection:
for collection in grocieres:
    for food in collection:
        print(food, end=" ")
    print()

# example 2:
num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()
