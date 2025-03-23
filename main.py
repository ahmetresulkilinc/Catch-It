import turtle
import random
import time

# Screen setup
screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Catch The Turtle")

FONT = ('Arial', 30, 'normal')

game_over = False


# Countdown Turtle
countdown_turtle = turtle.Turtle()

# Score Turtle setup
score_turtle = turtle.Turtle()
score = 0

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

    if not game_over:

        def click_turtle(x, y):
            global score
            score += 1
            score_turtle.clear()
            score_turtle.write(arg=f"Score: {score}", move=False, align="center", font=FONT)

            print(f"Kaplumbağa tıklandı: x = {x}, y = {y}")


        kaplumbaga.shape("turtle")
        kaplumbaga.speed(1)
        kaplumbaga.shapesize(2, 2)
        kaplumbaga.penup()

        degree = [30, 60, 90, 45, 71, 16, -30, -45, -60, -90, -270, -300, -238]
        forward = [50, 90, 150, 200, 300, 250, 125, 10]

        kaplumbaga.goto(random.randint(-200, 200), random.randint(-200, 200))
        kaplumbaga.showturtle()

        kaplumbaga.onclick(click_turtle)


        for i in range(20):
            kaplumbaga.hideturtle()
            kaplumbaga.penup()
            kaplumbaga.goto(random.randint(-200, 200), random.randint(-200, 200))
            kaplumbaga.showturtle()
            time.sleep(1)
            kaplumbaga.onclick(click_turtle)

def countdown(time):
    global game_over
    countdown_turtle.hideturtle()
    countdown_turtle.penup()

    top_height = screen.window_height() / 2
    y = top_height * 0.9

    countdown_turtle.setposition(0, y - 40)
    countdown_turtle.clear()
    if time  > 0:
        countdown_turtle.clear()
        countdown_turtle.write(arg="Time: {}".format(time), move=False, align="center", font=FONT)
        screen.ontimer(lambda: countdown(time - 1), 1000 )

    else:
        game_over = True
        countdown_turtle.clear()
        countdown_turtle.write(arg="Game Over!", move=False, align="center", font=FONT)




setup_score_turtle()
countdown(10)
make_turtle()


turtle.mainloop()
