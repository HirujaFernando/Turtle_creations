from emoji import emojize
from turtle import *

hideturtle()
emo = Screen()

def draw_square():
    width(5)
    color('red')
    goto(0, 300)
    goto(300, 300)
    color('blue')
    goto(300, 0)
    goto(0, 0)

draw_square()
penup()
goto(-350, 145)
color('black')
pendown()
write("Click anywhere on \n the screen.", font=('arial',25,'bold'))
penup()
goto(70, 135)

def emojies(x, y):
    color('purple')
    pendown
    a = emojize("Hello! \n Python is \n :thumbs_up::red_heart::cat:")
    write(a, font=('arial',20,'bold'))
emo.onclick(emojies)
done()
