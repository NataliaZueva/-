#import turtle
#turtle.shape("turtle")
#turtle.
#turtle.exitonclick()
n=input('Скольки угольник вы хотите увидеть? (число более 2) ')
n=int(n)
import turtle
t = turtle.Turtle()
t.hideturtle()
for i in range(2):
    t.fd(80)
    t.left(90)
    t.fd(30)
    t.left(90)
t.penup()
t.goto(11,7)
t.write("Push me", font=("Arial", 12))

def btnclick(x, y):
    if 0<x<80 and 0<y<30:
        print("Кнопка нажата!")
        t.clear()
        t.fillcolor('pink')
        t.pencolor('black')
        t.begin_fill()
        t.pendown()
        for i in range(n):
            t.forward(100)
            t.right(360/n)
        t.end_fill()
turtle.listen()
turtle.onscreenclick(btnclick, 1)
turtle.done()

