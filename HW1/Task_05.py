# Is year a leap year

year = int(input("Enter specific year: "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"Year {year} is a leap year.")
else:
    print(f"Year {year} is not a leap year.")