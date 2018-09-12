import turtle
jane = turtle.Pen()

sides = int(input("How many sides shall I draw? "))

for i in range(sides):
    jane.forward(20)
    jane.left(360 / sides)

