# Convert Celsius to Fahrenheit or Fahrenheit to Celsius

choice = input("Enter 'F' to convert Celsius to Fahrenheit or 'C' to convert Fahrenheit to Celsius: ")
if choice == "C":
    celsius = int(input("Enter temperature in Celsius to convert: "))
    result = celsius * 1.8 + 32
if choice == "F":
    fahrenheit = int(input("Enter temperature in Fahrenheit to convert: "))
    result = (fahrenheit - 32) / 1.8

print(f"The temperature is {result:.2f} degrees.")