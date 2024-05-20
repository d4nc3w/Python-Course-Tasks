import random

digits = []
alphabet = []
special = []

def generate_password(d, a, s, len):
    password = ""
    listOfChars = d + a + s
    for i in range(len):
        password += random.choice(listOfChars)
    return password

print(f"Welcome to password generator!")
print(f"Input wanted length of the password: ")
len = int(input())

print(f"Please select group of chars you want to use (0 to confirm): ")
choice = -1
i = 0
for i in range(3):
    print(f"(1) Digits")
    print(f"(2) Alphabet")
    print(f"(3) Special characters")
    print(f"(4) Confirm")
    i += 1
    choice = int(input())
    if choice == 1:
        dig = ("1234567890")
        for d in dig:
            digits.append(d)
    elif choice == 2:
        alph = ("abcdefghijklmnopqrstuvwxyz")
        for a in alph:
            alphabet.append(a)
    elif choice == 3:
        spe = ("!@#$%^&*()")
        for s in spe:
            special.append(s)
    elif choice == 4:
        print(f"Groups has been selected.")
        break

accept = -1
while accept != 1:
    password = generate_password(digits, alphabet, special, len)
    print(f"Generated password: {password}")
    accept = int(input("Accept? (1 - yes, 2 - no) "))

print(f"Success!")





