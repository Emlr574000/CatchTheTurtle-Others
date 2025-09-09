import turtle
drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Drawing Board")
turtle_instance = turtle.Turtle()


def Up():
    turtle_instance.setheading(turtle_instance.heading() - 10)
def Down():
    turtle_instance.setheading(turtle_instance.heading() + 10)
def Go():
    turtle_instance.forward(100)
def ClearScreen():
    turtle_instance.clear()
def turtle_return_home():
    return turtle_instance.home()
def turtle_pen_up():
    turtle_instance.penup()
def turtle_pen_down():
    turtle_instance.pendown()
drawing_board.listen()
drawing_board.onkey(fun=Go, key="space")
drawing_board.onkey(fun=Down, key="Left")
drawing_board.onkey(fun=Up, key="Right")
drawing_board.onkey(fun=ClearScreen, key="c")
drawing_board.onkey(fun=turtle_return_home, key="h")
drawing_board.onkey(fun=turtle_pen_up, key="u")
drawing_board.onkey(fun=turtle_pen_down, key="d")
turtle.done()