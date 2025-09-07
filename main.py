import turtle
from turtle import *

drawing_board=turtle.Screen()
drawing_board.bgcolor("black")
turtle.pencolor("pink")

for i in range(4):
    turtle.speed(11)
    if(i==0):
        for a in range(30):
            turtle.forward(5)
            turtle.left(90)
            turtle.forward(5)
            turtle.right(90)

    elif(i==1):

        for a in range(30):
            turtle.right(90)
            turtle.forward(5)

    turtle.circle(1, 180)