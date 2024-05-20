# BMI calculator

height = float(input("Enter your height: "))
weight = float(input("Enter your weight: "))

bmi = weight / (height ** 2)

print(f"Your bmi is {bmi}")