import turtle
import random
cem=turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("CatchTheTurtle The Game")
screen.listen()
cem.shape('turtle')
cem.speed("fastest")
cem.color("darkgreen")
cem.shapesize(stretch_wid=2, stretch_len=2,outline=2)

# Scoring


point=0
style = ('Courier', 30, 'italic')
score=turtle.Turtle()
score.penup()
score.hideturtle()
score.speed("fastest")
score.goto(-200, 250)
score.write(f"Points: {point}", font=style)
score.hideturtle()
score.speed(10)
def touch(x,y):
    global point
    point += 1
    score.clear()
    score.write(f"Points: {point}", font=style)

cem.onclick(touch)

def hareket():
    cem.hideturtle()
    cem.penup()
    cem.goto(random.randint(-200, 200), random.randint(-200, 200))
    cem.showturtle()
    screen.ontimer(hareket, 500)



hareket()
turtle.done()
