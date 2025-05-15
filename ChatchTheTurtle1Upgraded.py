import turtle
import random
from turtle import Screen,Turtle

turtle_screen=turtle.Screen()
turtle_screen.bgcolor("light green")
turtle_screen.title("Catch The Turtle")
turtle_screen.setup(width=1000,height=1000)

Font=("Arial",20,"normal")
score=0
game_active=False
time_left=0

text_turtle=turtle.Turtle()
text_turtle.hideturtle()
text_turtle.penup()
text_turtle.goto(0,400)



target_turtle=turtle.Turtle()
target_turtle.shape("turtle")
target_turtle.color("dark blue")
target_turtle.penup()
target_turtle.hideturtle()

def move_turtle():
    if game_active:
        random_location_x=random.randint(-480,480)
        random_location_y=random.randint(-480,480)
        target_turtle.hideturtle()
        target_turtle.goto(random_location_x,random_location_y)
        target_turtle.showturtle()
        turtle.ontimer(move_turtle,1000)
def increase_score(x,y):
    global score
    if game_active:
        score+=10
        update_display()

def update_display():
    text_turtle.clear()
    if game_active:
        text_turtle.write(f"Score:{score} | Time:{time_left}",align="center",font=Font)
    else:
        text_turtle.write(f"Click To Start! Last Score:{score}",align='center',font=Font)

def countdown(time):
    global time_left,game_active,score
    if not game_active:
        game_active=True
        score=0
        target_turtle.showturtle()
        move_turtle()
    time_left=time
    update_display()

    if time > 0:
        turtle.ontimer(lambda: countdown(time-1), 1000)
    else:
        game_active=False
        target_turtle.hideturtle()
        text_turtle.clear()
        text_turtle.write(f"Game Over! FinaL Score:{score} \click to play again",align='center',font=Font)
        target_turtle.hideturtle()

target_turtle.onclick(increase_score)
turtle_screen.onclick(lambda x,y:countdown(30) if not game_active else None)


update_display()
#screen is open
turtle.done()
