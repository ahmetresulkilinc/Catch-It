import turtle
import random
import time

#Screen
screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Catch The Turtle")

FONT = ('Arial', 30, 'normal')


#Score Turtle

score_turtle = turtle.Turtle()

def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.color("dark blue")
    score_turtle.penup()

    top_height = screen.window_height() / 2
    y = top_height * 0.9

    score_turtle.setposition(0, y)
    score_turtle.write(arg="Score: 0", move=False, align="center", font=FONT)


def make_turtle():
    kaplumbaga = turtle.Turtle()
    kaplumbaga.hideturtle()  # Başlangıçta kaplumbağa görünmesin
    kaplumbaga.shape("turtle")
    kaplumbaga.speed(1)
    kaplumbaga.shapesize(2, 2)

    degree = [30, 60, 90, 45, 71, 16, -30, -45, -60, -90, -270, -300]
    forward = [50, 90, 150, 200, 300, 250, 125]


    start_position = kaplumbaga.position()

    i = 1
    while i <= 20:
        kaplumbaga.hideturtle()

        kaplumbaga.penup()

        kaplumbaga.goto(start_position)

        selected_degree = random.choice(degree)
        selected_forward = random.choice(forward)

        kaplumbaga.left(selected_degree)
        kaplumbaga.forward(selected_forward)

        kaplumbaga.hideturtle()
        kaplumbaga.showturtle()
        time.sleep(1.5)
        i += 1




setup_score_turtle()
make_turtle()
turtle.mainloop()

