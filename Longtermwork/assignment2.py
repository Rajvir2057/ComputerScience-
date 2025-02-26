#Rajvir Kaur 816815
#importing important libraries.
import math
from turtle import *

t = Turtle() # this is a universal turtle that lets a person use the methods easily.
#creating variables 
length = 10
character_spacing = 10
linespacing = 45

# setup the turtle
t.width(5)
t.speed(10)
t.shape("turtle")
t.color("green")

#creating functions for each character
def R():
    seth(0)
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

def dummy():
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(length)

def movements():
    global x,y 
    x = x + character_spacing

    if x > 400:
        x = -50
        y = y - linespacing

    t.penup()
    t.goto(x, y)
    t.seth(-90)
    t.pendown()

x, y = -50,40
t.penup()
t.goto(x,y)
t.pendown()

#using user input and calling functions.
user_input = input("Enter your Name and student id: ")
for char in user_input:
    movements()
    if char == "R":
        R()
    elif char == "A":
        A()
    elif char == "J":
        J()
    elif char == "V":
        V()
    elif char == "I":
        I()
    elif char == "R":
        R()
    elif char == "K":
        K()
    elif char == "A":
        A()
    elif char == "U":
        U()
    elif char == "R":
        R()
    elif char == "8":
        eight()
    elif char == "1":   
        one()
    elif char == "6":
        six()
    elif char == "5":
        five()
    elif char == " ":
        x = -50 - character_spacing
        y = y - linespacing
    else:
        dummy()

    x = x+ character_spacing
    t.penup()

done()


