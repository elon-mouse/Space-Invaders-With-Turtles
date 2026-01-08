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

laser = turtle.Turtle()
laser.speed(7)
laser.color("red")

def laser(x,y):
    x = ship.xcor()
    y = ship.ycor()
    laser.goto(x,y)
    laser.left(90)
    laser.forward(10000000)

def right():
    x = ship.xcor()
    y = ship.ycor()
    ship.goto(x+15,y)
    
def left():
    x = ship.xcor()
    y = ship.ycor()
    ship.goto(x-15,y)

wn.onkey(laser, "space")

wn.onkeypress(right, "Right")

wn.onkeypress(left, "Left")

wn.listen()
wn.mainloop()