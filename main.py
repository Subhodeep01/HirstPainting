# import colorgram as cg
#
# colors = cg.extract("image.jpg", 30)
from turtle import Turtle, Screen, colormode
import random

turtle = Turtle()
turtle.speed(0)

colormode(255)
color_list = [(245, 242, 235), (230, 235, 243), (245, 236, 241), (235, 244, 239), (210, 158, 90), (236, 214, 96),
              (38, 104, 147), (151, 77, 55), (127, 168, 196), (205, 136, 162), (152, 62, 83), (23, 39, 54),
              (174, 161, 50), (209, 87, 65), (197, 87, 118), (56, 117, 91), (137, 182, 151), (25, 44, 36),
              (63, 45, 34), (227, 169, 186), (238, 212, 6), (88, 156, 102), (36, 164, 187), (41, 59, 101),
              (12, 97, 73), (180, 189, 212), (227, 175, 167), (96, 126, 171), (65, 34, 44), (107, 42, 58)]

# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     new_color = (r, g, b)
#     color_list.append(new_color)
#
# print(color_list)
turtle.penup()
turtle.setpos(-250, -250)
ini_x = turtle.xcor()
ini_y = turtle.ycor()

for i in range(11):
    turtle.setx(ini_x)
    ini_y = turtle.ycor()
    for j in range(11):
        turtle.pendown()
        colors = random.choice(color_list)
        turtle.pencolor(colors)
        turtle.dot(20)
        turtle.penup()
        turtle.forward(50)

    turtle.sety(ini_y + 50)

screen = Screen()

screen.exitonclick()