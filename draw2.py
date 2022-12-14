import turtle
import random

tim = turtle.Turtle()
tim.speed(3)
tim.width(5)

def up():
    tim.setheading(90)
    tim.forward(100)

def down():
    tim.setheading(270)
    tim.forward(100)

def left():
    tim.setheading(180)
    tim.forward(100)

def right():
    tim.setheading(0)
    tim.forward(100)

colors = ["red","blue","green","yellow","black"]

def clickLeft(x,y):
    tim.color(random.choice(colors))

def clickRight(x,y):
    tim.stamp()

turtle.listen()

turtle.onscreenclick(clickLeft, 1)
turtle.onscreenclick(clickRight, 3)

turtle.onkey(up, "Up")
turtle.onkey(down, "Down")
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")

turtle.done()
turtle.mainloop()
