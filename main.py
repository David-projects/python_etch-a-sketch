from turtle import Turtle, Screen
from etch_a_sketch import EtchASketch

sam = Turtle()
screen = Screen()
screen.listen()
e = EtchASketch(sam, screen)

screen.onkeypress(key='w', fun=e.move_forward)
screen.onkeypress(key='s', fun=e.move_backwards)
screen.onkeypress(key='a', fun=e.turn_right)
screen.onkeypress(key='d', fun=e.turn_left)
screen.onkeypress(key='c', fun=e.clear_screen)






screen.exitonclick()