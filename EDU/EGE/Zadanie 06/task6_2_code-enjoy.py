from turtle import *
tracer(0) # начать рисовать сразу же
# перемещение Ч в левый (-300) нижний (-200) угол экрана, а то её в этой программе не видно

penup()
goto(-300,-200)
pendown()

left(90) # первоначально Ч смотрит влево вдоль ОХ

k=20 # коэффициент для визуального наблюдения
for i in range(2):
    forward(10*k)
    right(90)
    forward(18*k)
    right(90)
penup()
forward(5*k)
right(90)
forward(7*k)
left(90)
pendown()
for i in range(2):
    forward(10*k)
    right(90)
    forward(7*k)
    right(90)

# Рисование сетки точками
penup()
for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x*k, y*k)
        dot(4, 'red')
