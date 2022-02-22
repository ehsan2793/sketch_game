from turtle import Turtle, Screen

screen = Screen()
jim = Turtle()
# screen color and color settings
screen.bgcolor('black')
screen.colormode(255)


def move_forward():
    jim.forward(10)

def left_turn():
    jim.left(10)

def right_turn():
    jim.right(10)

def draw_circle():
    jim.circle(10)
def move_back():
    jim.backward(10)

def clear_screen():
    jim.clear()
    jim.penup()
    jim.setposition(0,0)
    jim.pendown()
screen.listen()
screen.onkey(fun=move_forward, key="Up")
screen.onkey(fun=move_back, key="Down")
screen.onkey(fun=right_turn, key="Right")
screen.onkey(fun=left_turn, key="Left")
screen.onkey(fun=left_turn, key="Left")

screen.onkey(fun=draw_circle, key="space")
screen.onkey(fun=clear_screen, key="c")
jim.color((255, 200, 23))

screen.exitonclick()
