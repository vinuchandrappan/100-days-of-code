from turtle import Screen, Turtle
import random
import turtle

is_race_is_on=False

screen=Screen()
screen.setup(width=500, height=400)
user_bet=screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")
print(user_bet)
colors=["red", "yellow", "blue", "green", "purple", "orange"]
y_position=[-70, -40, -10, 20, 50, 80]
all_turtles=[]

for turtle_index in range(0, 6):
  tim=Turtle(shape="turtle")
  tim.penup()
  tim.color(colors[turtle_index])
  tim.goto(x=-230,y=y_position[turtle_index])
  all_turtles.append(tim)
  
  
if user_bet:
  is_race_is_on=True

while is_race_is_on:
    
  for turtle in all_turtles:
    if turtle.xcor()>230:
        is_race_is_on=False
        winning_color=turtle.pencolor()
        if winning_color==user_bet:
          print(f"You won! The {winning_color} turtle is the winner!")
        else:
           print(f"You lost! The {winning_color} turtle is the winner!") 
           
    
    rand_distance=random.randint(0, 10)
    turtle.forward(rand_distance)
  
screen.exitonclick()