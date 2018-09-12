#We start by making an empty list
myBackpack = []

#Next we ask for the first item, and store it in a variable called 'item'
item = (input("""Hail adventurer! Before we set sail, you will need
to pack your backpack. What is the first item you would
like to pack? """))

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

print("Actually, I don't think you need a " + myBackpack[1] +
      ". I'm going to replace it with a map. Here is what you've packed:")

#Assign "map" to the second item in the list
myBackpack[1] = "map"
print(myBackpack)
