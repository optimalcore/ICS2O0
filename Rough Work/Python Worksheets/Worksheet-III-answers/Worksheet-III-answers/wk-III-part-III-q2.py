shoppingList = []

numberOfItems = int(input("How many items would you like to add? "))

for i in range(numberOfItems):
    item = input("Add item: ")
    shoppingList.append(item)

print("You have added the following items to your shopping list:")
print(shoppingList)

