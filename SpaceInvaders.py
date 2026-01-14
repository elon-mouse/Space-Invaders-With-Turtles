import turtle
import random
import time


wn = turtle.Screen()
ship = turtle.Turtle()
wn.setup(width=1920, height=1080)
wn.bgcolor("black")
wn.title("SPACE_INVADERS")
ship.color("red")
ship.speed(0)
ship.left(90)
ship.penup()
ship.goto(0,-200)

list2=[]

for i in range(12):
    enemy = turtle.Turtle()
    enemy.showturtle()
    enemy.speed(0)
    enemy.shape("circle")
    enemy.penup()
    list2.append(enemy)
    enemy.color("grey")
    enemy.goto(-30*i,15)
for i in range(12):
    enemy = turtle.Turtle()
    enemy.showturtle()
    enemy.speed(0)
    enemy.shape("circle")
    enemy.penup()
    list2.append(enemy)
    enemy.color("grey")
    enemy.goto(30*i,15)

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


wn.onkeypress(right, "Right")
wn.onkeypress(left, "Left")
wn.onkeypress(bullet, "space") 

keepgoing = True
def gameloop():
    global keepgoing 
    for b in list1:
        b.showturtle()
        b.goto(b.xcor(),b.ycor()+20)
        for e in list2: 
            if (e.ycor()-b.ycor())<=2:
                if abs(e.xcor()-b.xcor())<=2:
                    e.hideturtle()
                    list2.remove(e)

    wn.update() 
    if keepgoing: 
        wn.ontimer(gameloop, 16)
gameloop()
wn.listen()
wn.mainloop()