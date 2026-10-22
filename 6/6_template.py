from turtle import *
#-----------
#Эти строки в налаче надо писать ВСЕГДА
tracer(0)
SCALE = 15
left(90)
#-----------

#---------------
#Далее это действия, которые выполняет черепаха
for _ in range(6):
    forward(24 * SCALE)
    right(90)
    forward(30 * SCALE)
    right(90)

up()

forward(2 * SCALE)
right(90)
forward(10 * SCALE)
left(90)

down()

for _ in range(6):
    forward(75 * SCALE)
    right(90)
    forward(71 * SCALE)
    right(90)
#---------------------

#------------------
#отрисовка поля
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * SCALE, y * SCALE)
        dot(4, "red")


update()
done()
#----------------
