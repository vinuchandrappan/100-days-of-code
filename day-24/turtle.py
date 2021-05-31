from turtle import Turtle, Screen
import random
import turtle

tim=Turtle()
turtle.colormode(255)

colours=["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

'''Square'''
# tim.forward(100)
# tim.left(90)
# tim.forward(100)
# tim.left(90)
# tim.forward(100)
# tim.left(90)
# tim.forward(100)
# tim.left(90)
'''Dotted line'''
# for _ in range(10):
#   tim.forward(10)
#   tim.penup()
#   tim.forward(10)
#   tim.pendown()

'''Shapes'''
# def draw_shape(num_of_sides):
#   angle=360/num_of_sides
#   for _ in range(num_of_sides):
#     tim.forward(100)
#     tim.right(angle)
# for shape_in_side_n in range(3, 11):
#   tim.color(random.choice(colours))
#   draw_shape(shape_in_side_n)

'''Random walk'''
directions=[0, 90, 180, 270]
def random_color():
  r=random.randint(0, 255)
  g=random.randint(0, 255)
  b=random.randint(0, 255)
  random_color=(r, g , b)
  return random_color
  
  
tim.pensize(10)
tim.speed("fastest")
for _ in range(200):
  tim.color(random_color())
  tim.forward(30)
  tim.setheading(random.choice(directions)) 



screen=Screen()
screen.exitonclick()
