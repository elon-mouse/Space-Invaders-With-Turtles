import turtle
import random
import time


wn = turtle.Screen()
ship = turtle.Turtle()
wn.setup(width=480, height=640)
wn.bgcolor("black")
wn.title("SPACE_INVADERS")
ship.color("red")
ship.speed(0)
ship.left(90)
ship.penup()
ship.goto(0,-200)


for i in range(7):
    enemy = turtle.Turtle()
    enemy.showturtle()
    enemy.speed(0)
    enemy.shape("circle")
    enemy.penup()
    enemy.color("grey")
    enemy.goto(-30*i,30*i)


list1=[]

def bullet():
    laser = turtle.Turtle()
    laser.hideturtle()
    laser.color("red")
    laser.shape("circle")
    laser.left(90)
    laser.penup()
    list1.append(laser)
    x = ship.xcor()
    y = ship.ycor()
    laser.speed(0)
    laser.goto(x,y)
    laser.showturtle()

    
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

keepgoing = True
def gameloop():
    global keepgoing 
    for b in list1:
        b.showturtle()
        b.forward(30)
    wn.update() 
    if keepgoing: 
        wn.ontimer(gameloop, 16)
gameloop()
wn.listen()
wn.mainloop()