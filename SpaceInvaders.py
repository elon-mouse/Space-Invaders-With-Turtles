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

text = turtle.Turtle()
text.hideturtle()
text.color("white")
text.penup()
text.goto(0,0)

list2=[]


start_time = time.time()

for i in range(6):
    for j in range(8):
        enemy = turtle.Turtle()
        enemy.showturtle()
        enemy.speed(0)
        enemy.shape("circle")
        enemy.penup()
        list2.append(enemy)
        enemy.color("grey")
        enemy.goto(-30*i,30*j)

for i in range(6):
    for j in range(8):
        enemy = turtle.Turtle()
        enemy.showturtle()
        enemy.speed(0)
        enemy.shape("circle")
        enemy.penup()
        list2.append(enemy)
        enemy.color("grey")
        enemy.goto(30*i+30,30*j)

list3=[]

enemyCooldown = False
def resetEnemyCooldown():
    global enemyCooldown
    enemyCooldown = False

def enemyShoot():
    global enemyCooldown
    if enemyCooldown == False and len(list2) > 0:
        enemyCooldown = True
        wn.ontimer(resetEnemyCooldown, 1000)
        enemyshoot = random.choice(list2)
        bullet = turtle.Turtle()
        bullet.hideturtle()
        bullet.color("green")
        bullet.shape("circle")
        bullet.penup()
        bullet.speed(0)
        bullet.goto(enemyshoot.xcor(), enemyshoot.ycor())
        bullet.showturtle()
        list3.append(bullet)


list1=[]

cooldown = False
def changeCooldown():
    global cooldown
    cooldown = False


def bullet():
    global cooldown
    if cooldown == False:
        cooldown = True
        wn.ontimer(changeCooldown, 1000)
        laser = turtle.Turtle()
        laser.hideturtle()
        laser.color("red")
        laser.shape("circle")
        laser.left(90)
        laser.penup()
        x = ship.xcor()
        y = ship.ycor()
        laser.speed(0)
        laser.goto(x,y)
        list1.append(laser)
        laser.showturtle()

cooldown1 = False
def changeCooldown1():
    global cooldown1
    cooldown1 = False

def enemymovedown():
    global cooldown1
    if cooldown1 == False:
        cooldown1 = True
        wn.ontimer(changeCooldown1, 20000)
        for e in list2:
            x = e.xcor()
            y = e.ycor()
            e.goto(x,y-30)


def right():
    x = ship.xcor()
    y = ship.ycor()
    ship.goto(x+30,y)

def left():
    x = ship.xcor()
    y = ship.ycor()
    ship.goto(x-30,y)

wn.score=0
wn.title("Space Invaders. Score: {0}".format(wn.score))

wn.onkeypress(right, "Right")
wn.onkeypress(right, "d")
wn.onkeypress(left, "Left")
wn.onkeypress(left, "a")
wn.onkeypress(bullet, "space")

keepgoing = True
def gameloop():
    wn.title("Space Invaders. Score: {0}".format(wn.score))
    global keepgoing
    
    enemymovedown()
    enemyShoot()

    for eb in list3:
        eb.goto(eb.xcor(), eb.ycor()-15)

        if eb.ycor() < -540:
            eb.hideturtle()
            list3.remove(eb)

        if eb.distance(ship) < 20:
            keepgoing = False
            eb.hideturtle()
            text.clear()
            elapsed_time = round(time.time() - start_time, 1)
            text.goto(0,400)
            text.write("GAME OVER\nYou survived for {0} seconds".format(elapsed_time), align="center", font=("Arial", 48, "bold"))
            wn.title("GAME OVER")
            break


    for b in list1:
        b.showturtle()
        b.goto(b.xcor(),b.ycor()+20)

        if b.ycor() > 540:
            b.hideturtle()
            list1.remove(b)

        for e in list2:
            if b.distance(e) < 15:
                wn.score+=1
                e.hideturtle()
                list2.remove(e)
                b.hideturtle()
                list1.remove(b)

                if len(list2) == 0:
                    keepgoing = False
                    text.clear()
                    elapsed_time = round(time.time() - start_time, 1)
                    text.write("YOU WIN!\nFinal Score: {0}\nTime taken to win {0} seconds".format(wn.score), align="center", font=("Arial", 48, "bold"))
                    wn.title("YOU WIN! Final Score: {0}".format(wn.score))
                break

    wn.update()
    if keepgoing:
        wn.ontimer(gameloop, 16)

gameloop()
wn.listen()
wn.mainloop()