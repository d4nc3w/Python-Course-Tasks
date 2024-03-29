# function = A block of reusable code place () after the function name toi invoke it
# return = statement used to end a function and send a result back to the caller

# 1
def happy_birthday(name, age):
    print(f"Happy Birthday to {name}!")
    print(f"You are {age} years old.")
    print("Happy Birthday to you!")
    print()

happy_birthday("Piotr", 30)

# 2
def display_invoice(username, amount, due_date):
    print(f"Hello {username}.")
    print(f"Your bill ${amount:.2f} is due: {due_date}")

display_invoice("d4nc3w", 42.50, "30/01/2025")

# 3
def add(x, y):
    z = x+y
    return z

def subtract(x, y):
    z = x - y
    return z
def divide(x, y):
    z = x / y
    return z

def multiply(x, y):
    z = x * y
    return z

print(add(9, 2))
print(subtract(80, 4))
print(divide(52, 2))
print(multiply(2, 16))

# 4
def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("piotr", "dancewicz")
print(full_name)

# ----------------------------------------------

def adder(a, b):
    return a + b


class ZeroArg(Exception):
    pass

class ZeroDenom(Exception):
    pass

def f(num, denom):
    if denom == 0:
        raise ZeroDenom
    elif num == 0:
        raise ZeroArg

i = 0
while i < 5:
    i += 1
else:
    print("Break")

word = "Python"
for letter in word:
    print(letter, end=" ")

fourSeasons = {'Spring' : 'E major', 'Summer' : 'G major',
               'Autumn' : 'F# minor', 'Winter' : 'F minor'}

print()
for key, value in fourSeasons.items():
    print(key + " - " + value)

