import turtle

wn = turtle.Screen()
ship = turtle.Turtle()
wn.setup(width=1920, height=1080)
wn.bgcolor("white")
wn.title("SPACE_INVADERS")
ship.color("red")
ship.speed(0)
ship.left(90)
ship.penup()
import random
import time

rng = random.Random()

enemy = []
for i in range(25):
    a = turtle.Turtle()
    a.hideturtle()
    a.speed(0)
    a.shape("circle")
    a.penup()
    a.color("grey")
    x=rng.randrange(-5,5)
    y=rng.randrange(0,10)
    a.goto(x*100,y*100)
    enemy.append(a)
    a.showturtle()

laser = turtle.Turtle()
laser.color("red")
laser.shape("circle")
laser.left(90)
laser.penup()

def bullet():
    x = ship.xcor()
    y = ship.ycor()
    laser.speed(0)
    laser.goto(x,y)
    laser.speed(2)
    laser.forward(10000)
    

def right():
    x = ship.xcor()
    y = ship.ycor()
    ship.goto(x+15,y)
    
def left():
    x = ship.xcor()
    y = ship.ycor()
    ship.goto(x-15,y)

wn.onkeypress(bullet, "space") 

wn.onkeypress(right, "Right")

wn.onkeypress(left, "Left")

wn.listen()
wn.mainloop()