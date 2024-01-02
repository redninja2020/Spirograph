from turtle import Turtle, Screen
import turtle as t
import random

timmy_the_turtle = Turtle()
t.colormode(255)
timmy_the_turtle.shape("classic")
timmy_the_turtle.pensize(1)
timmy_the_turtle.speed('fastest')

def pen_colour():
    timmy_the_turtle.color((random.randint(0,255), random.randint(0,255), random.randint(0,255)))

def draw_circle(size):
    for i in range(int(360/size)):
        pen_colour()
        timmy_the_turtle.circle(100)
        timmy_the_turtle.setheading(timmy_the_turtle.heading()+size)        





draw_circle(3)

screen = Screen()
screen.exitonclick()