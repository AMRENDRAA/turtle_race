import turtle
from turtle import Turtle,Screen
import random
is_race_on =False
new_turtles=Screen()
screen=Screen()
screen.setup(width=500,height=400)

user_bet=screen.textinput(title="make your bet",prompt="which turtle color will win")
colors=["red","orange","yellow","green","blue","purple"]
y_positions=[-70,-40,-10,20,50,80]
all_turtles=[]
for turtle_index in range(0,6):
    new_turtles=Turtle(shape="turtle")
    new_turtles.color(colors[turtle_index])
    new_turtles.penup()
    new_turtles.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtles)

if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on=False
            winning_color=turtle.pencolor()
            if winning_color==user_bet:
                print(f" you have won ! the {winning_color} turtle is winner")
            else:
                print(f"you have lost {winning_color}   turtle is winner")
        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance)





screen.exitonclick()