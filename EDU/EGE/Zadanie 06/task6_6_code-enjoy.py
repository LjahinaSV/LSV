from turtle import *

tracer(0)
k=6
left(90)
penup()
goto(-100,-100) 
pendown()
for i in range(21):
    forward(31*k)
    right(60)
penup()
       

for x in range(-60,60):
    for y in range(-60,60):
        setpos(x*k,y*k)
        dot(2,'red')
