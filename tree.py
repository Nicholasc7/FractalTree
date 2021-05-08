import turtle
import time


def init_screen():
    win = turtle.Screen()
    win.setup(800, 800)
    win.title("Fractal Tree ^.^")
    win.bgcolor("light blue")


def tree():
    # Creates trunk of tree
    trunk = turtle.Turtle()
    trunk.pensize(2.2)
    trunk.speed(0)
    trunk.shapesize(.5)
    trunk.penup()
    trunk.color("black")
    trunk.left(90)
    trunk.goto(0, -350)
    trunk.pendown()
    trunk.speed(7)
    trunk.forward(350)
    return trunk.pos()


# Recipe for branches. Starts at (0, 0), facing upright
def spawn_branch():
    branch = turtle.Turtle()
    branch.pensize(2.2)
    branch.speed(0)
    branch.shapesize(.5)
    branch.pendown()
    branch.color("dark green")
    branch.left(90)
    return branch


def fractal():
    ANGLE = 20
    MOVE = 135
    tick = 2

    branch_a = spawn_branch()
    branch_b = spawn_branch()
    branch_a.left(ANGLE)
    branch_a.forward(MOVE)
    branch_b.right(ANGLE)
    branch_b.forward(MOVE)
    apos = branch_a.pos()
    bpos = branch_b.pos()
    MOVE -= 25

    for i in range(tick):
        a = spawn_branch()
        a.penup()
        b = spawn_branch()
        b.penup()
        a.setpos(apos)
        b.setpos(bpos)
        a.pendown()
        b.pendown()

        for i in range(tick)
            a.left(ANGLE*tick)
            a.forward(MOVE)
            b.right(ANGLE*tick)
            b.forward(MOVE)







init_screen()

fractal()
time.sleep(1.3)
