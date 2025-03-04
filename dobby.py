from turtle import *

def draw_circle(color, x, y, radius):
    penup()
    goto(x, y - radius)
    pendown()
    fillcolor(color)
    begin_fill()
    circle(radius)
    end_fill()

def move(x, y):
    penup()
    goto(x, y)
    pendown()

def wrinkle(offset_x, offset_y):
    left(90)
    circle(16, 25)
    left(180)
    circle(16, -50)
    left(180)
    circle(16, 25)

def draw_dobby(x, y):#s=80
    clear()
    speed(0)
    hideturtle()
    #bgcolor("pink")

    # Head
    penup()
    goto(x, y)
    pendown()
    setheading(0)
    fillcolor("pink")
    begin_fill()
    circle(32,5)
    circle(32,-10)
    circle(16,-70)
    right(180)
    forward(24)
    right(180)
    circle(12,-90)

    penup()
    goto(x, y)
    pendown()
    setheading(0)
    circle(32,5)
    circle(16,70)
    forward(24)
    circle(12,90)

    circle(56,30)
    end_fill()

    setheading(0)

    # Eyes
    draw_circle("white",x-10, y+32, 7)
    draw_circle("white", x+10, y+32, 7)
    draw_circle("black", x-10, y+32, 4)
    draw_circle("black", x+10, y+32, 4)

    # Nose
    penup()
    goto(x, y+30)
    pendown()
    right(50)
    forward(8)
    circle(20, 50)
    right(175)
    forward(20)

    # Mouth
    penup()
    goto(x-6,y+12)
    setheading(0)
    pendown()
    pensize(3)
    fillcolor("red")
    begin_fill()
    forward(16)
    left(90)
    circle(8, -180)
    end_fill()

    # Wrinkles
    pensize(1)
    move(x-14, y+44)
    wrinkle(x, y)

    move(x-14, y+42)
    setheading(270)
    wrinkle(x,y)

    move(x-14, y+46)
    setheading(270)
    wrinkle(x, y)

    # Left Ear
    move(x-38, y+40)
    right(180)
    fillcolor("pink")
    begin_fill()
    circle(30, -30)
    circle(30, 70)
    #end_fill()

    setheading(0)
    penup()
    forward(8)
    right(90)
    forward(8)
    pendown()
    setheading(90)
    circle(8, 90)
    circle(8, -90)
    setheading(270)
    circle(18, 140)
    end_fill()

    # Right Ear
    setheading(0)
    move(x+38, y+40)
    right(180)
    fillcolor("pink")
    begin_fill()
    circle(30,30)
    circle(30,-70)

    setheading(0)
    penup()
    forward(-8)
    right(90)
    forward(8)
    pendown()
    setheading(-90)
    circle(8,-90)
    circle(8,90)

    setheading(-270)
    circle(18,-140)
    end_fill()

if __name__ == "__main__":
    draw_dobby(100,1000)  # Example: Draw Dobby at (0, 0)
