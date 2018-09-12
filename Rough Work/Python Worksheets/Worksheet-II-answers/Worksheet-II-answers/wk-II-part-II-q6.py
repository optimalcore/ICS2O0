#We start by making an empty list
myBackpack = []

#Next we ask for the first item, and store it in a variable called 'item_0'
item_0 = input("""Hail adventurer! Before we set sail, you will need
to pack your backpack. What is the first
item you would like to pack? """)

#Now let's add the item to our list
myBackpack.append(item_0)

#Let's get the next item from the user, and add it to our list.
#We'll store it in a new variable 'item_1'
item_1 = input("Ok great. What next? ")

myBackpack.append(item_1)

#Do the same for the final item
item_2 = input("Never leave home without a " + myBackpack[1] + " hey?" +
             " Great, there should be enough room for one more. ")

myBackpack.append(item_2)

#Tell the user we want to get rid of the second item we added.
#Remember, we stored this in the variable 'item_1'
print("Oops. I don't think we have room for a " + item_1 + ". I'll take that out")

#Remove the item from the list, and show the list
myBackpack.remove(item_1)
print("You have left:")
print(myBackpack)
