
name = "Piotr Dancewicz"

# length of string
length = len(name)
print(length)

# first position of char in string
char1 = name.find("i")
print(char1)

# last position of char in string
char2 = name.rfind("i")
print(char2)

# make only first letter in upper case
cname = name.capitalize()
print(cname)

# make string fully in upper case
uname = name.upper()
print(uname)

# make string fully in lower case
lname = name.lower()
print(lname)

# return true if string only contains digit
result = name.isdigit()
print(result)
num = "123456789"
result = num.isdigit()
print(result)

# return true if string only contain letters
result2 = name.isalpha()
print(result2)
name2 = "Piotr"
result3 = name2.isalpha()
print(result3)

# counts specific chars in string
result4 = name.count("i")
print(result4)

# replace specific chars with another
phoneNum = "111-222-333"
print(phoneNum)
phoneNum = phoneNum.replace("-", "|")
print(phoneNum)

# list of methods
print(help(str))

