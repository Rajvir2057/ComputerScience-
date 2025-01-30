#Rajvir Kaur 816815
#importing important libraries.
import math
from turtle import *

t = Turtle() # this is a universal turtle that lets a person use the methods easily.
#creating variables 
length = 10
character_spacing = 50

#creating functions for each character
def R():
    t.forward(length*2)
    t.back(length)
    t.left(90)
    t.right(45)
    t.forward(math.sqrt(length ** 2 + length ** 2))
    t.back(math.sqrt(length ** 2 + length ** 2))
    t.left(45)
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(length)

def A():
    t.forward(length * 2)
    t.back(length * 2)
    t.left(90)
    t.forward(length)
    t.right(90)
    t.forward(length * 2)
    t.back(length)
    t.right(90)
    t.forward(length)

def J():
    t.penup()
    t.forward(length)
    t.pendown()
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(length * 2)

def V():
    t.forward(length * 2)
    t.left(90 + 45)
    t.forward(math.sqrt(length ** 2 + length ** 2))
    t.left(45)
    t.forward(length)
def I():
    t.left(90)
    t.forward(length)
    t.back(length / 2)
    t.right(90)
    t.forward(length * 2)
    t.right(90)
    t.back(length / 2)
    t.forward(length)

def K():
    t.forward(length*2)
    t.back(length)
    t.left(90)
    t.right(45)
    t.forward(math.sqrt(length ** 2 + length ** 2))
    t.back(math.sqrt(length ** 2 + length ** 2))
    t.left(90)
    t.forward(math.sqrt(length ** 2 + length ** 2))

def U():
    t.forward(length*2)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(length*2)

def eight():
    t.forward(length * 2)
    t.back(length * 2)
    t.left(90)
    t.forward(length)
    t.right(90)
    t.forward(length * 2)
    t.back(length)
    t.right(90)
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(length)

def one():
    t.left(90)
    t.forward(length / 2)
    t.right(90)
    t.forward(length*2)
    t.right(90)
    t.forward(length/2)
    t.back(length)

def six():
    t.left(90)
    t.forward(length)
    t.back(length)
    t.right(90)
    t.forward(length * 2)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(length)

def five():
    t.left(90)
    t.forward(length)
    t.back(length)
    t.right(90)
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(length)

def triangle():
    t.begin_fill()
    t.fillcolor("#FFB6C1")
    t.left(90)
    t.forward(50)
    t.left(120)
    t.forward(50)
    t.left(120)
    t.forward(50)
    t.left(120)
    t.end_fill()

def rectangle():
    t.forward(50)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(100)
    t.left(90)

def circle():
    t.circle(50)
def starting_position(x, y):
    """ This function moves to the next character position """
    t.penup()
    t.setx(character_spacing * x)
    t.sety(character_spacing * y)
    t.seth(-90)
    t.pendown()

# setup the turtle
t.width(5)
t.speed(10)
t.shape("turtle")
t.color("#ADD8E6")


# initialize the position of the turtle
x = 0
y = 0

# draw the text
starting_position(-4, 0)
R()
starting_position(-3, 0)
A()
starting_position(-2, 0)
J()
starting_position(-1, 0)
V()
starting_position(0, 0)
I()
starting_position(1, 0)
R()
starting_position(-4, -1)
K()
starting_position(-3, -1)
A()
starting_position(-2, -1)
U()
starting_position(-1, -1)
R()

starting_position(2, -2)
eight()
starting_position(3, -2)
one()
starting_position(4, -2)
six()
starting_position(5, -2)
eight()
starting_position(6, -2)
one()
starting_position(7, -2)
five()
#shapes
starting_position(-4, -4)
triangle()
starting_position(-3, -4)
rectangle()
starting_position(-1, -4)
circle()

#using turtle done to let the window send
done()