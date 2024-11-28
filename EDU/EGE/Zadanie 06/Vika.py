from turtle import *

tracer (0)
k=15
left (90)
pendown()
for i in range(4):
    forward(10*k)
    right(60)
    forward(10*k)
    right (120)

penup()
for x in range (-30, 30) :
    for y in  range(-30,30):
        setpos( x*k, y*k)
        dot(4, 'red')
