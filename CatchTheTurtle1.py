import turtle
import random
from turtle import Screen,Turtle

turtle_screen=turtle.Screen()
turtle_screen.bgcolor("light green")
turtle_screen.title("Catch The Turtle")
turtle_screen.setup(width=1000,height=1000)

Font=("Arial",20,"normal")



def countdown(time):
    turtle_screen.onclick(None)
    turtle.clear()

    if time > 0:
        turtle.write(time,align="center",font=Font)
        turtle_screen.ontimer(lambda: countdown(time-1), 1000)
    else:
        turtle.write("Game Over",align='center',font=Font)
        turtle_screen.onclick(lambda x,y:countdown(30))




random_location_x=random.randint(-480,480)
random_location_y=random.randint(-480,480)








screen=turtle.Screen()
screen.onclick(lambda x,y:countdown(30))

t=turtle.Turtle()
t.shape("turtle")
t.color("dark blue")
t.hideturtle()
t.goto(random_location_x,random_location_y)
t.showturtle()


turtle.done()