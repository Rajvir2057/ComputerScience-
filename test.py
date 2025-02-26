#student name : simranjeet kaur
#student id : 817229

from turtle import *
import math

letter_space = 15
line_spacing = 50

# setup the turtle
speed(6)
shape("circle")
color("red")

#creating functions for each character
def S():
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)
    right(90)
    forward(50)
    right(90)
    forward(50)

def I():
    forward(50)
    backward(25)
    right(90)
    forward(50)
    left(90)
    forward(25)
    backward(50)

def M():
    left(90)
    forward(100)
    right(135)
    forward(70)
    left(90)
    forward(70)
    right(135)
    forward(100)

def R():
    forward(50)
    back(50)
    left(90)
    right(45)
    forward(math.sqrt(50**2 + 50**2))
    back(math.sqrt(50**2 + 50**2))
    left(45)
    forward(50)
    left(90)
    forward(50)
    
def A():
    left(90)
    forward(50)
    back(50 / 2)
    right(90)
    forward(50* 2)
    right(90)
    back(50 / 2)
    forward(50)

def N():
    left(90)
    forward(100)  
    right(135)
    forward(140)  
    forward(100) 

def eight():
    forward(50 * 2)
    back(50 * 2)
    left(90)
    forward(50)
    right(90)
    forward(50 * 2)
    back(50)
    right(90)
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)

def one():
    left(90)
    forward(50 / 2)
    right(90)
    forward(50*2)
    right(90)
    forward(50/2)
    back(50)

def seven():
    forward(50)  
    right(90)         
    forward(100) 

def two():
    forward(50)  
    right(90)
    forward(50)
    right(90)
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50) 
def nine():
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

def dummy():
    circle(50)

def movements():
    global x,y 
    x = x + letter_space

    if x > 400:
        x = -50
        y = y - line_spacing

    penup()
    goto(x, y)
    seth(-90)
    pendown()

x, y = -50,40
penup()
goto(x,y)
pendown()

#using user input and calling functions.
user_input = input("Enter your Name and student id: ")
for char in user_input:
    movements()
    if char == "S":
        S()
    elif char == "I":
        I()
    elif char == "M":
        M()
    elif char == "R":
        R()
    elif char == "A":
        A()
    elif char == "N":
        N()
    elif char == "8":
        eight()
    elif char == "1":   
        one()
    elif char == "7":
        seven()
    elif char == "2":
        two()
    elif char == "9":
        nine()
    elif char == " ":
        x = -50 - letter_space
        y = y - line_spacing
    else:
        dummy()

    x = x+ letter_space
    penup()

done()