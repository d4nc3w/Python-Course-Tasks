# Integer -> binary and counts the number of set bits

num = int(input("Enter a number: "))
count = 0
binary = ""

while num != 0:
    if num % 2 == 1:
        count += 1
    binary = str(num % 2) + binary
    num = num // 2

print(f"The number of set bits is {count}. The binary representation is: {binary}")
