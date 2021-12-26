#from math import *
import math
from turtle import *
speed(0)
hideturtle()
while True:
    try:
        a,k=input('ведите(a) и (k)\n').split()
        a=float(a)
        k=float(k)
    except ValueError:
        print('Попробуйте еще раз...')
    else:
        up()
        i=0
        while i < 3000:
            pa=math.radians(k*i)
            pp=math.sin(pa)
            p = a * (pp)
            forward(p)
            dot(3)
            goto(0,0)
            if abs(pp) < 1:
                left(1)
            else:
                left(2)
            i+=1
                
                
     
