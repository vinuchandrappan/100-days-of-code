from turtle import Turtle,  Screen, position
from snake import Snake
import time

screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake=Snake()


screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_is_on=True  
while game_is_on:
  screen.update()
  time.sleep(.1) 
  snake.mov()







screen.exitonclick()