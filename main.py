import turtle
import random
screen = turtle.Screen()
screen.title("Catch the turtle")
screen.bgcolor("light blue")
style = ('Courier', 30, 'italic')
score = 0
game_over = False
#turtle_list
turtle_list = []

#countdownturtle
countdown_turtle = turtle.Turtle()

#make_turtle_propeties
x_coordonates = [-20,-10,0,10,20]
y_coordinates = [20,10,0,-10,20]

#Score Turtle
score_turtle = turtle.Turtle()

grid_size=10

def setup_scor_turtle():
    score_turtle.hideturtle()
    score_turtle.color("red")
    score_turtle.penup()
    top_height = screen.window_height()/2

    y = top_height*0.8
    score_turtle.setpos(0, y)
    score_turtle.write(arg="Score:0",move=False,align="left",font=style)

def make_turtle(x,y):
    t = turtle.Turtle()
    def handle_turtle(x, y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(f"Score:{score}".format(score), move=False, align="left", font=style)
        #print(x, y)
    t.onclick(handle_turtle)
    t.shape("turtle")
    t.penup()
    t.shapesize(2,2)
    t.color("green")
    t.goto(x*grid_size, y*grid_size)
    turtle_list.append(t)

def setup_turtles():
    for x in x_coordonates:
        for y in y_coordinates:
            make_turtle(x, y)

def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

def show_turtle_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtle_randomly, 1000)

def countdown(time):
    global game_over
    countdown_turtle.color("yellow")
    countdown_turtle.penup()
    top_height = screen.window_height() / 2
    y = top_height * 0.7
    countdown_turtle.setpos(0, y-30)
    countdown_turtle.hideturtle()
    countdown_turtle.clear()
    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write("Time:{}".format(time), move=False, align="left", font=style)
        screen.ontimer(lambda: countdown(time - 1), 1000)

    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write("Game over", move=False, align="left", font=style)


def start_game_up():
    global game_over
    game_over = False
    turtle.tracer(0)
    setup_turtles()
    hide_turtles()
    setup_scor_turtle()
    show_turtle_randomly()
    countdown(10)
    turtle.tracer(1)

start_game_up()

turtle.mainloop()