import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("lightblue")

# Create a turtle object
pen = turtle.Turtle()
pen.shape("classic")
pen.color("orange")
pen.speed(3)

# Draw a square
for _ in range(4):
    pen.forward(100)
    pen.right(90)

# Exit on click
screen.exitonclick()
# turtle has north south west east
