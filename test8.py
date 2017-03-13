import turtle
def draw_square(angie):
    for i in range(0,4):
        angie.forward(100)
        angie.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("blue")

    brad = turtle.Turtle()
    brad.shape("arrow")
    brad.color("orange")
    brad.speed(10)
    
    for i in range(0,36):
        draw_square(brad)
        brad.right(10)

    window.exitonclick()

         
draw_art()



