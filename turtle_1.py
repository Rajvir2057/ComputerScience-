from turtle import *

t = Turtle()
'''''
t.circle = circle(90,360)

done()


t.penup()
t.goto(-300, 300)

t.pendown() '''''

'''''
for steps in range(100):
    for c in ('blue', 'red', 'green'):
        color(c)
        forward(steps)
        right(30)
done()'''''
'''''
t.home()

t.dot()
t.fd(50); t.dot(20, "blue"); t.fd(50)
t.position()
(100.00,-0.00)
t.heading()'''
'''''
t.color("blue")
stamp_id = t.stamp()
t.fd(50)
'''
''''
t.pensize(20)
t.shape("turtle")
t.circle(50,360)
t.color("red")

done()'''
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
backward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
done()
