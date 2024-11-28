from turtle import *
tracer(0)
k=50
left(90)
for i in range(16):
    left(36)
    forward(4*k)
    left(36)

penup()
for x in range(-10, 10):
    for y in range(-10, 10):
        setpos(x*k, y*k)
        dot(4, 'red')
# 31
# pendown()
# backward()
# goto(x,y)
# right(120)
