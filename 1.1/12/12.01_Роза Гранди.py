def drawCircles(t,size):
    for i in range(rang):
        t.circle(size)
        size = size - num
def drawSpecial(t,size, repeat):
    for i in range(repeat):
        drawCircles(t,size)
        t. right(rotate/repeat)



import turtle
import math
import random
wn = turtle.Screen()
wn.bgcolor('black')



#1 round
roun = turtle.Turtle()
roun.speed(0)
roun.color('darkred')
rotate = int(360)
num = 4
rang = 10
drawSpecial(roun,100,10)

#2 round
roun = turtle.Turtle()
roun.speed(0)
roun.color('crimson')
rotate = int(360)
num = 4
rang = 10
drawSpecial(roun,80,9)

#3 round
roun = turtle.Turtle()
roun.speed(0)
roun.color('coral')
rotate = int(360)
num = 4
rang = 10
drawSpecial(roun,60,8)


#4 round
roun = turtle.Turtle()
roun.speed(0)
roun.color('pink')
rotate = int(360)
num = 4
rang = 10
drawSpecial(roun,40,7)

#5 round
roun = turtle.Turtle()
roun.speed(0)
roun.color('yellow')
rotate = int(360)
num = 2
rang = 10
drawSpecial(roun,1,5)









