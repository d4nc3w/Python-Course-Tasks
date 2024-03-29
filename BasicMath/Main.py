import math

Apples = 10
print(type(Apples))

# worse version
Apples = 10 + 1
print(Apples)

# better version
Apples += 1
print(Apples)

Apples *= 5
print(Apples)

Apples /= 2
print(Apples)
print(type(Apples))

Apples = 4
# to the power 2
Apples **= 2
print(Apples)

remainder = Apples % 3
print(remainder)

# Basic math functions
x = 3.14
y = 4
z = 5

result = round(x)
print(result)

y = -4
result = abs(x)
print(result)

toPower = pow(4, 3)
print(toPower)

maxVal = max(x, y, z)
minVal = min(x, y, z)
print(maxVal,  minVal)

# using math library
print(math.pi)
print(math.e)

x = 9
result = math.sqrt(x)
print(result)
result =  math.ceil(x)
print(result)
result = math.floor(x)
print(result)

radius = float(input("Enter radius: "))
circumference = 2 * math.pi * radius
area = math.pi * pow(radius, 2)
print(f"The circumference is: {round(circumference, 2)}cm")
print(f"The area is: {round(area, 2)}cm^2")

