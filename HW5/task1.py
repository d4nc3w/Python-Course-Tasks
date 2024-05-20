file_path = 'list.txt'

class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

def addProduct(product):
    shoppingList.append(product)
    with open(file_path, 'a') as file:
        file.write(f"{product.name}\t{product.quantity}\n")

def removeProduct(name):
    for product in shoppingList:
        if product.name == name:
            shoppingList.remove(product)
            print(f"{name} removed from the shopping list.")
            return
    print(f"{name} not found in the shopping list.")

def displayShoppingList():
    with open(file_path, 'r') as file:
        for line in file:
            data = line.strip().split('\t')
            print(f"Product: {data[0]}, Quantity: {data[1]}")

def saveShoppingListToFile():
    with open(file_path, 'w') as file:
        for product in shoppingList:
            file.write(f"{product.name}\t{product.quantity}\n")

def exitProgram():
    print("Exiting the program...")

shoppingList = []
try:
    with open(file_path, 'r') as file:
        for line in file:
            data = line.strip().split('\t')
            shoppingList.append(Product(data[0], data[1]))
except FileNotFoundError:
    print("File not found. Creating a new one.")

while True:
    print("------Shopping List App------")
    print("(1) Add product")
    print("(2) Remove product")
    print("(3) Display shopping list")
    print("(4) Save shopping list to file")
    print("(5) Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter product name: ")
        quantity = input("Enter quantity: ")
        if quantity.isdigit():
            product = Product(name, quantity)
            addProduct(product)
        else:
            print("Invalid quantity. Please enter a numeric value.")
    elif choice == '2':
        name = input("Enter product name to remove: ")
        removeProduct(name)
    elif choice == '3':
        displayShoppingList()
    elif choice == '4':
        saveShoppingListToFile()
        print("Shopping list saved to file.")
    elif choice == '5':
        exitProgram()
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
