import turtle
import time

wn = turtle.Screen()
wn.setup(800, 600)
wn.bgcolor("black")
wn.title("Stuff")
wn.tracer(0)
wn.listen()

pen1 = turtle.Turtle()
pen1.penup()
pen1.color("white")
pen1.hideturtle()

pen2 = turtle.Turtle()
pen2.penup()
pen2.color("white")
pen2.hideturtle()

pen3 = turtle.Turtle()
pen3.penup()
pen3.color("white")
pen3.hideturtle()

pen4 = turtle.Turtle()
pen4.penup()
pen4.color("white")
pen4.hideturtle()

pen5 = turtle.Turtle()
pen5.penup()
pen5.color("white")
pen5.hideturtle()

pen6 = turtle.Turtle()
pen6.penup()
pen6.color("white")
pen6.hideturtle()

pen7 = turtle.Turtle()
pen7.penup()
pen7.color("white")
pen7.hideturtle()

pen8 = turtle.Turtle()
pen8.penup()
pen8.color("white")
pen8.hideturtle()

pen9 = turtle.Turtle()
pen9.penup()
pen9.color("white")
pen9.hideturtle()

pen10 = turtle.Turtle()
pen10.penup()
pen10.color("white")
pen10.hideturtle()

marker = turtle.Turtle()
marker.color("red")
marker.shape("square")
marker.shapesize(stretch_len=.1, stretch_wid=.1)
marker.penup()
marker.speed(0)
marker.hideturtle()


def timer():
    now = time.localtime(time.time())
    return now[5]


def erase():
    marker.pendown()
    marker.hideturtle()
    marker.color("black")


def write():
    marker.pendown()
    marker.showturtle()
    marker.color("red")


def move(x, y):
    marker.penup()
    marker.goto(x, y)
    marker.pendown()


def start():
    pen1.clear()
    pen1.write("Stuff!", align="center", font=("Courier", 30, "normal"))
    pen2.clear()
    pen2.goto(0, -35)
    pen2.write("Press Space to Start", align="center", font=("Courier", 15, "normal"))
    wn.onkeypress(instructions, "space")


def instructions():
    pen1.clear()
    pen2.clear()
    pen1.goto(0, 100)
    pen2.goto(0, 75)
    pen3.goto(0, 50)
    pen4.goto(0, 25)
    pen5.goto(0, 0)
    pen6.goto(0, -25)
    pen7.goto(0, -50)
    pen8.goto(0, -75)
    pen9.goto(0, -100)
    pen10.goto(0, -150)
    pen1.write("Press \"e\" to erase", align="center", font=("Courier", 16, "normal"))
    pen2.write("Press \"w\" to write", align="center", font=("Courier", 16, "normal"))
    pen3.write("Press \"u\" to lift pen", align="center", font=("Courier", 16, "normal"))
    pen4.write("Press \"d\" to drop pen", align="center", font=("Courier", 16, "normal"))
    pen5.write("Press \"h\" to hide marker", align="center", font=("Courier", 16, "normal"))
    pen6.write("Press \"s\" to show marker", align="center", font=("Courier", 16, "normal"))
    pen7.write("Press \"c\" to clear", align="center", font=("Courier", 16, "normal"))
    pen8.write("Press \"z\" to undo", align="center", font=("Courier", 16, "normal"))
    pen9.write("Press \"q\" to quit", align="center", font=("Courier", 16, "normal"))
    pen10.write("Click and Drag Marker to Write", align="center", font=("Courier", 16, "normal"))
    wn.onkeypress(main, "space")


def main():
    wn.onkeypress(erase, "e")
    wn.onkeypress(write, "w")
    wn.onkeypress(marker.penup, "u")
    wn.onkeypress(marker.pendown, "d")
    wn.onkeypress(marker.hideturtle, "h")
    wn.onkeypress(marker.showturtle, "s")
    wn.onkeypress(marker.clear, "c")
    wn.onkeypress(wn.bye, "q")
    wn.onkeypress(marker.undo, "z")
    pen1.clear()
    pen2.clear()
    pen3.clear()
    pen4.clear()
    pen5.clear()
    pen6.clear()
    pen7.clear()
    pen8.clear()
    pen9.clear()
    pen10.clear()
    marker.goto(350, 260)
    marker.clear()
    marker.pendown()
    marker.showturtle()
    while 1:
        wn.update()
        if marker.ycor() >= 285:
            marker.sety(285)
        if marker.ycor() <= -275:
            marker.sety(-275)
        if marker.xcor() >= 375:
            marker.setx(375)
        if marker.xcor() <= -385:
            marker.setx(-385)


def up():
    y = marker.ycor()
    y += 5
    marker.sety(y)


def down():
    y = marker.ycor()
    y -= 5
    marker.sety(y)


def left():
    x = marker.xcor()
    x -= 5
    marker.setx(x)


def right():
    x = marker.xcor()
    x += 5
    marker.setx(x)


start()
wn.onclick(move)
marker.ondrag(marker.goto)
wn.onkeypress(up, "Up")
wn.onkeypress(down, "Down")
wn.onkeypress(left, "Left")
wn.onkeypress(right, "Right")

while 1:
    wn.update()
