# while loop = execute some code WHILE some condition remains true

name = input("Enter your name: ")

while name == "":
    print("You did not enter your name!")
    name = input("Enter your name: ")
else:
    print(f"Hello {name}")

# second example
age = int(input("Enter your age: "))
while age <= 0:
    print("You cant have less than or equal to 0")
    age = int(input("Enter your age: "))
else:
    print(f"You are {age} years old")

# third example
food = input("Enter your favorite food (q to quit): ")
while not food == "q":
    print(f"You like {food}")
    food = input("Enter antoher food you like (q to quit): ")

print(food)