import turtle as turtle_module
from turtle import Screen
import random

tim = turtle_module.Turtle()
turtle_module.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()
screen = Screen()
screen.bgcolor('black')

colors = [(248, 247, 246), (250, 240, 246), (234, 242, 248), (241, 250, 246), (21, 114, 174), (142, 163, 184), (204, 137,
                                                                                                                167), (192, 174, 15), (148, 16, 31), (68, 23, 31), (16, 139, 58), (237, 212, 66), (216, 160, 93), (50, 28, 26), (122, 71,
                                                                                                                                                                                                                                 101), (198, 66, 28), (6, 107, 64), (228, 168, 197), (243, 216, 3), (25, 179, 89), (241, 74, 29), (20, 172, 189), (111,
                                                                                                                                                                                                                                                                                                                                                   191, 142), (183, 94, 116), (188, 181, 214), (35, 37, 46), (157, 206, 216), (138, 26, 21), (238, 168, 156), (9, 101, 105)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 101


for dot_count in range(1, number_of_dots):
    tim.dot(20, random.choice(colors))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen.exitonclick()
