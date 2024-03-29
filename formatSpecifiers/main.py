# format specifiers = {value:flags} format a value based on what flags are inserted

price1 = 3.14159
price2 = -987.656
price3 = 12.34
price4 = 15.3432
price5 = 1200.32

# output has exatcly 10 spaces to display itself
print(f"Price 1 is ${price1:10}")
# output is rounded up to 2 spaces after dot
print(f"Price 2 is ${price2:.2f}")
# outpat has exactly 10 spaces to display and ^ centers them
print(f"Price 3 is ${price3:^10}")
# the output has + before its value if the number is positive
print(f"Price 4 is ${price4:+}")
# each thosuand in output is separated using comma
print(f"Price 5 is ${price5:,}")