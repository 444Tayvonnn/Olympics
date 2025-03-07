import turtle

screen = turtle.Screen()
screen.screensize(500,500)
screen.bgcolor('tan')

t = turtle.Turtle()


# Set up the screen
screen = turtle.Screen()
screen.title("Olympic Rings")
screen.bgcolor("tan")  # Set the background color to tan

# Create a turtle object
ring_turtle = turtle.Turtle()
ring_turtle.pensize(2)  # Set the pen size to make the circles thinner

# Function to draw a ring
def draw_ring(color, x, y):
    ring_turtle.penup()
    ring_turtle.color(color)
    ring_turtle.goto(x, y)
    ring_turtle.pendown()
    ring_turtle.circle(50)


# Draw the Olympic rings
colors = ["blue", "black", "red", "yellow", "green"]
positions = [(-120, 0), (0, 0), (120, 0), (-60, -50), (60, -50)]

for color, (x, y) in zip(colors, positions):
    draw_ring(color, x, y)

# Add text for "Winter Olympics" at the top in purple
ring_turtle.penup()
ring_turtle.goto(0, 100)
ring_turtle.pendown()
ring_turtle.color("purple")
ring_turtle.write("Winter Olympics", align="center", font=("Arial", 24, "bold"))

# Add text for "2026" at the bottom in purple
ring_turtle.penup()
ring_turtle.goto(0, -150)
ring_turtle.pendown()
ring_turtle.write("2026", align="center", font=("Arial", 24, "bold"))

# Hide the turtle and display the window
ring_turtle.hideturtle()
turtle.done()