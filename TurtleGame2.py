import turtle
import random
screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Catch The Turtle")

Font=("Arial", 28, "normal"),
#score list
score=0
game_over=False
#countdown turtle
countdown_turtle=turtle.Turtle()


#turtle list
turtle_list=[]




#score turtle
def setup_score_turtle():
    global score_turtle
    score_turtle = turtle.Turtle()
    score_turtle.hideturtle()
    score_turtle.color("dark blue")
    score_turtle.penup()
    top_height = screen.window_height() / 2
    y=top_height * 0.9

    score_turtle.setpos(0,y)
    score_turtle.write("Score: 0",move=False, align="center", font=Font)
grid_size=10
def make_turtle(x,y):
    t=turtle.Turtle()

    def handle_click(x,y):
        global score
        score+=1
        score_turtle.clear()
        score_turtle.write(arg="Score: {}".format(score),move=False, align="center", font=Font)
        #print(x,y)
    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(2,2)
    t.color("dark green")
    t.goto(x*grid_size,y*grid_size)
    turtle_list.append(t)

def setup_turtles():
    x_cordinate=[-40,-20,0,20,40]
    y_cordinate=[20,10,0,-10,-20]

    for x in x_cordinate:
        for y in y_cordinate:
            make_turtle(x,y)

def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

#recursive  function yaptık fakat çıkış noktası olması gerekir
def show_turtles_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtles_randomly, 500)
    else:
        hide_turtles()

def countdown(time):
    global game_over
    countdown_turtle.hideturtle()
    countdown_turtle.penup()
    top_height = screen.window_height() / 2
    y = top_height * 0.9
    countdown_turtle.setpos(0, y-30)
    countdown_turtle.clear()
    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write("Time:  {}".format(time), move=False, align="center", font=Font)
        screen.ontimer(lambda:countdown(time-1),1000)
    else:
        game_over=True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write("Game Over", move=False, align="center", font=Font)




def start_game_up():
    turtle.tracer(0)
    setup_score_turtle()
    setup_turtles()
    hide_turtles()
    show_turtles_randomly()
    countdown(10)
    turtle.tracer(1)


start_game_up()
turtle.mainloop()