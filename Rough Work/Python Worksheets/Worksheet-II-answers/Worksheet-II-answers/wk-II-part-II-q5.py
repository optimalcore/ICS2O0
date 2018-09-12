#We start by making an empty list
myBackpack = []

#Next we ask for the first item, and store it in a variable called 'item'
item = input("""Hail adventurer! Before we set sail, you will need
to pack your backpack. What is the firstitem you would
like to pack? """)

#Now let's add the item to our list
myBackpack.append(item)

#Let's get the next item from the user, and add it to our list.
#We can reuse the variable 'item'
item = input("Ok great. What next? ")

myBackpack.append(item)

#Do the same for the final item
item = input("Never leave home without a " + myBackpack[1] + " hey?" +
             " Great, there should be enough room for one more. ")
myBackpack.append(item)

#Lastly, we print the contents of the list
print("Fantastic! You have packed: ")
print(myBackpack)
print("Good luck!")
