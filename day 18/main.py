
import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
tim.shape("turtle")
tim.color("red")

# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
colors = ["red", "orange", "yellow", "green", "blue",
          "purple", "black", "Slategray", "SeaGreen", "DeepSkyBlue"]


# def draw_shape(num_sides):
#     angle = 360/num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)


# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_side_n)
directions = [0, 90, 180, 270]
tim.pensize(3)
tim.speed("fastest")
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

for i in range(100):
    tim.color(random_color())
    tim.circle(100)
    tim.left(10)
    tim.hideturtle()


screen = Screen()
screen.exitonclick()
