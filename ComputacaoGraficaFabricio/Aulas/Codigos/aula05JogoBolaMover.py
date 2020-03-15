from turtle import Turtle, Screen

screen = Screen()
screen.setup(1200, 500)

# Ground

ground = Turtle()
ground.speed('fastest')

ground.penup()
ground.goto(-1000, -200)
ground.pendown()
ground.forward(2000)

# Player

player = Turtle()
player.speed('fastest')

PlayerX = -600

def moveX():
    global PlayerX

    screen.onkeypress(None, "w") # disable handler in handler
    player.clear()
    player.penup()
    player.goto(PlayerX, -99)
    player.pendown()
    player.color("Slate Gray")
    player.begin_fill()
    player.circle(-50)
    player.end_fill()

    PlayerX += 10
    screen.onkeypress(moveX, "w")
    # reenable handler


screen.listen()
moveX()
screen.mainloop() # change import & use turtle.mainloop() if Python 2