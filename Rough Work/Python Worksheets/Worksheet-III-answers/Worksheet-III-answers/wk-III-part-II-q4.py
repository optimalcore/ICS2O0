number = int(input("Choose a number between 0 and 10: "))

for i in range(-number, 0):
    print(str(i) + " is negative")
    
for i in range(0, number + 1):
    print(str(i) + " is positive")

