import random
# 1
low = 1
high = 6
num = random.randint(low, high)
print(num)

# 2
num2 = random.random()
print(num2)

# 3
options = ("rock", "paper", "scissors")
choice = random.choice(options)
print(choice)

# 4
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
random.shuffle(cards)
print(cards)

min = 1
max = 100
count = 0
number = random.randint(min, max)

while True:
    guess = int(input(f"Enter a number between {min} and {max}: "))
    count += 1

    if guess < number:
        print(f"{guess} is too low")
    elif guess > number:
        print(f"{guess} is too high")
    else:
        print(f"{guess} is correct")
        break

print(f"This round took you {count} guesses")
