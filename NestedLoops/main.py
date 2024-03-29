# nested loop = A loop within another loop

# each element ends not with /n (default) but with space
for x in reversed(range(1, 10)):
    print(x, end=" ")
print()

for x in range(3):
    for y in range(1, 10):
        print(y, end=" ")
    print()