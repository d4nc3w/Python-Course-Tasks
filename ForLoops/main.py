# for loops = execute a block of code a fixed number of times
#             you can iterate over a range, string, sequence, etc.

# 1st example:
for count in range(1, 11):
    print(count)
print(" ")

# 2nd example:
for counter in reversed(range(1, 11)):
    print(counter)
print("HAPPY NEW YEAR")

# 3rd example:
for x in range(1, 11, 3):
    print(x)

print(" ")

# 4th example:
credit_card = "1234-5678-4321-9876"
for x in credit_card:
    print(x)

# 5th example:
for x in range (1, 21):
    if x == 13:
        break
    else:
        print(x)
