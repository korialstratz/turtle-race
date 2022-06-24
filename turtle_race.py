from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Choose", prompt="Which turtle is going to win?: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_list = []
race_on = False


def make_turtle(tcolor, cy):
    turtles = Turtle(shape="turtle")
    turtles.color(tcolor)
    turtles.penup()
    turtles.goto(x=-230, y=cy)
    return turtle_list.append(turtles)


def move_turtle(t_list):
    distance = random.randint(1, 10)
    random.choice(t_list).forward(distance)


def check_winner(wcolor, ucolor):
    if wcolor == ucolor:
        print(f"The winning turtle is {ucolor}, You win!!! ")
    else:
        print(f"The winning turtle is {wcolor}, You loose!!! ")


y = -220
for color in colors:
    y = y + 60
    make_turtle(color, y)

if user_bet:
    race_on = True
    while race_on:
        for turtle in turtle_list:
            if turtle.xcor() >= 230:
                winning_color = turtle.color()[0]
                check_winner(winning_color, user_bet)
                race_on = False
            move_turtle(turtle_list)

# tim = Turtle(shape="turtle")
# tim.penup()
# tim.goto(x=-230, y=-160)

screen.exitonclick()
