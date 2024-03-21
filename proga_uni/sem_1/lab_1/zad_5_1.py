import math
import turtle

for i in range(6):
    turtle.forward(200)
    turtle.left(90)

turtle.right(90)

turtle.left(45)
turtle.forward((200*math.sqrt(2)/2))
turtle.left(90)
turtle.forward((200*math.sqrt(2)/2))

turtle.left(90)
turtle.forward((200*math.sqrt(2)))
turtle.left(90+45)
turtle.forward(200)
turtle.left(90+45)
turtle.forward((200*math.sqrt(2)))