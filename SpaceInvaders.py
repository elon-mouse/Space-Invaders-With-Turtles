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
laser.color("red")
laser.shape("circle")

def bullet():
    x = ship.xcor()
    y = ship.ycor()
    laser.speed(0)
    laser.goto(x,y)
    laser.speed(7)
    laser.left(90)
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