from turtle import Screen, Turtle
import turtle
import random
from typing import Sized

timm=Turtle()
turtle.colormode(255)

def random_color():
  r=random.randint(0, 255)
  g=random.randint(0, 255)
  b=random.randint(0, 255)
  color=(r, g, b)
  return color

timm.speed("fastest")
def draw_spirograph(size_of_the_gap):
  for _ in range(int(360/size_of_the_gap)):
    timm.color(random_color())
    timm.circle(100)
    timm.setheading(timm.heading()+size_of_the_gap)
    
draw_spirograph(5)



screen=Screen()
screen.exitonclick()