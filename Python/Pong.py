import turtle
import random
import time


wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)
wn.listen()

paddle1 = turtle.Turtle()
paddle1.shape("square")
paddle1.speed(0)
paddle1.color("white")
paddle1.shapesize(stretch_len=1, stretch_wid=5)
paddle1.penup()
paddle1.hideturtle()

paddle2 = turtle.Turtle()
paddle2.shape("square")
paddle2.speed(0)
paddle2.color("white")
paddle2.shapesize(stretch_len=1, stretch_wid=5)
paddle2.penup()
paddle2.hideturtle()

ball = turtle.Turtle()
ball.shape("circle")
ball.speed(0)
ball.color("white")
ball.penup()
ball.hideturtle()

pen1 = turtle.Turtle()
pen1.speed(0)
pen1.color("white")
pen1.penup()
pen1.hideturtle()

pen2 = turtle.Turtle()
pen2.speed(0)
pen2.color("white")
pen2.penup()
pen2.hideturtle()

pen3 = turtle.Turtle()
pen3.speed(0)
pen3.color("white")
pen3.penup()
pen3.hideturtle()

pen4 = turtle.Turtle()
pen4.speed(0)
pen4.color("white")
pen4.penup()
pen4.hideturtle()


def timer():
    now = time.localtime(time.time())
    return now[5]


def start():
    pen1.clear()
    pen1.write("Welcome to Pong!!", align="center", font=("Courier", 30, "normal"))
    pen2.clear()
    pen2.goto(0, -35)
    pen2.write("Press Space to Start", align="center", font=("Courier", 15, "normal"))
    wn.onkeypress(instructions, "space")


def instructions():
    pen1.clear()
    pen1.goto(0, 50)
    pen1.write("How to Play", align="center", font=("Courier", 30, "normal"))
    pen2.clear()
    pen2.goto(0, 0)
    pen2.write("Your paddle will follow the cursor up and down.\nScore 3 points before the computer does to win!",
               align="center", font=("Courier", 15, "normal"))
    pen4.clear()
    pen4.goto(0, -35)
    pen4.write("Press \"q\" to quit at anytime", align="center", font=("Courier", 15, "normal"))
    pen3.clear()
    pen3.goto(0, -75)
    pen3.write("Press Space", align="center", font=("Courier", 15, "normal"))
    wn.onkeypress(reset, "space")


def reset():
    time.sleep(0.1)
    paddle1.showturtle()
    paddle2.showturtle()
    ball.showturtle()
    paddle1.goto(-360, 0)
    paddle2.goto(350, 0)
    ball.goto(0, 0)
    pen1.clear()
    pen1.goto(0, 250)
    pen1.write("Computer: 0  Player: 0", align="center", font=("Courier", 24, "normal"))
    pen2.clear()
    pen3.clear()
    pen4.clear()
    ball.dx = -8
    ball.dy = random.choice([-8, 8])
    paddle1.dy = 6.5
    main_loop()


def main_loop():
    score1 = 0
    score2 = 0
    while 1:
        wn.update()
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        if ball.ycor() > paddle1.ycor():
            paddle1.sety(paddle1.ycor() + paddle1.dy)
        if ball.ycor() < paddle1.ycor():
            paddle1.sety(paddle1.ycor() - paddle1.dy)

        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
        if ball.ycor() < -280:
            ball.sety(-280)
            ball.dy *= -1

        if ball.xcor() > 375:
            score1 += 1
            pen1.clear()
            pen1.write("Computer: {}  Player: {}".format(score1, score2), align="center",
                       font=("Courier", 24, "normal"))
            ball.dx = -8
            ball.dy = random.choice([-8, 8])
            ball.setx(375)
            ball.goto(0, 0)
            paddle1.goto(-360, 0)
            paddle1.dy = random.uniform(6.85, 6.9)
        if ball.xcor() < -385:
            score2 += 1
            pen1.clear()
            pen1.write("Computer: {}  Player: {}".format(score1, score2), align="center",
                       font=("Courier", 24, "normal"))
            ball.dx = 8
            ball.dy = random.choice([-8, 8])
            ball.setx(-385)
            ball.goto(0, 0)
            paddle1.goto(-360, 0)
            paddle1.dy = random.uniform(6.85, 6.9)

        if paddle1.ycor() < -235:
            paddle1.sety(-235)
        if paddle1.ycor() > 245:
            paddle1.sety(245)
        if paddle2.ycor() < -235:
            paddle2.sety(-235)
        if paddle2.ycor() > 245:
            paddle2.sety(245)

        if 330 < ball.xcor() < 345 and paddle2.ycor() - 60 < ball.ycor() < paddle2.ycor() + 60:
            ball.setx(330)
            ball.dx = -ball.dx - 1
        if -355 < ball.xcor() < -340 and paddle1.ycor() - 60 < ball.ycor() < paddle1.ycor() + 60:
            ball.setx(-340)
            ball.dx = -ball.dx + 1
            paddle1.dy += .05

        if ball.dx >= 22:
            ball.dx = 22
        elif ball.dx <= -22:
            ball.dx = -22

        if score1 == 3 or score2 == 3:
            paddle1.hideturtle()
            paddle2.hideturtle()
            ball.hideturtle()
            ball.goto(0, 0)
            timer()
            if score1 == 3:
                pen1.clear()
                pen1.goto(0, 0)
                pen1.write("You Lose!!", align="center", font=("Courier", 36, "normal"))
                pen2.clear()
                pen2.goto(0, -35)
                pen2.write("Press Space to Restart", align="center", font=("Courier", 18, "normal"))
                pen3.clear()
                pen3.goto(0, -75)
                pen3.write("Game ends in: {}".format(59 - int(timer())), align="center", font=("Courier", 15, "normal"))
                time.sleep(0.1)
            if score2 == 3:
                pen1.clear()
                pen1.goto(0, 0)
                pen1.write("You Win!!", align="center", font=("Courier", 36, "normal"))
                pen2.clear()
                pen2.goto(0, -35)
                pen2.write("Press Space to Restart", align="center", font=("Courier", 18, "normal"))
                pen3.clear()
                pen3.goto(0, -75)
                pen3.write("Game ends in: {}".format(59 - int(timer())), align="center", font=("Courier", 15, "normal"))
                time.sleep(0.1)
            if timer() == 59:
                wn.bye()


def move(self, fun):
    def event_fun(event):
        fun(350, -event.y + 300 / self.yscale)
    self.cv.bind("<Motion>", event_fun)


def move_pos(x, y):
    move(wn, None)
    paddle2.goto(x, y)
    move(wn, move_pos)


start()
move(wn, move_pos)
wn.onkeypress(wn.bye, "q")

while 1:
    wn.update()
