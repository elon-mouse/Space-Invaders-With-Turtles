import turtle
import random
import time


wn = turtle.Screen()
ship = turtle.Turtle()
wn.setup(width=1280, height=960)
wn.bgcolor("white")
wn.title("SPACE_INVADERS")
ship.color("red")
ship.speed(0)
ship.left(90)
ship.penup()



for i in range(7):
    enemy = turtle.Turtle()
    enemy.showturtle()
    enemy.hideturtle()
    enemy.speed(0)
    enemy.shape("circle")
    enemy.penup()
    enemy.color("grey")
    enemy.goto(-30+i,30+i)


laser = turtle.Turtle()
laser.color("red")
laser.shape("circle")
laser.left(90)
laser.penup()
laser.hideturtle()

def bullet():
    x = ship.xcor()
    y = ship.ycor()
    laser.speed(0)
    laser.goto(x,y)
    laser.speed(2)
    laser.showturtle()
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