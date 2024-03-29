# name = input("Enter your name: ")
# # input is always considered to be a string (we will cast age to int)
# age = int(input("Enter your age: "))
#
# print("Hello " + name + "!")
# # different version of print method:
# print(f"Your age is {age}.")
#
# timeLeft = 50 - age
# print(f"You will be 50 years old in {timeLeft} years.")
#
# # area calc
# length = float(input("Enter your length: "))
# width = float(input("Enter your width: "))
#
# area = length * width
# print(f"Your area is {area} cm^2")

#shopping cart
item = input("What item would you like to buy? ")
price = float(input("What is the price? "))
quantity = int(input("How many items would you like? "))

total = price * quantity
print(f"You have bought {quantity} x {item} /s")
print(f"Your total cost is: ${round(total, 2)}")