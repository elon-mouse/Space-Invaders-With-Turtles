import turtle

wn = turtle.Screen()
ship = turtle.Turtle()

wn.bgcolor("white")
wn.title("SPACE_INVADERS")
ship.color("red")
ship.speed(5)
ship.left(90)
ship.penup()

def right():
    x = ship.xcor()
    y = ship.ycor()
    ship.goto(x+15,y)
    
def left():
    x = ship.xcor()
    y = ship.ycor()
    ship.goto(x-15,y)

wn.onkey(right, "Right")

wn.onkey(left, "Left")

wn.listen()
wn.mainloop()