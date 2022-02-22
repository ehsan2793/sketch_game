import random
import turtle
from turtle import Turtle, Screen, color, distance

color_arr = ['red', 'blue', 'green', 'brown', 'black', 'orange', 'purple']
screen = Screen()
screen.setup(width=500, height=400)
screen.colormode(255)
color_Bet = screen.textinput('Make a Bet', 'what color will win? ')

all_turtles = []
y = 140
for i in range(6):
    jim = Turtle('turtle')
    jim.penup()
    jim.color(color_arr[i])
    jim.setposition(x=-230, y=y)
    y -= 50
    all_turtles.append(jim)
game_on = True
while game_on:
    for each_turtle in all_turtles:
        dis = random.randint(0, 10)
        each_turtle.forward(dis)
        if each_turtle.xcor() >= 225:
            winner_color = each_turtle.pencolor()
            if color_Bet == winner_color:
                print(f'you guessed right {winner_color} turtle won ')
            else:
                print(f'you lose the winner was {winner_color} turtle')
            game_on = False

screen.exitonclick()
