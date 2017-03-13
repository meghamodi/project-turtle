import turtle                        # importing the turtle module

def draw_square(angie):             # for drawing  a square
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
    
    for i in range(0,36):              # for creating circle taking 36 squares
        draw_square(brad)
        brad.right(10)                 # rotating squares at an angle of 10 degree at right         

    window.exitonclick()              # click on the window to exit

         
draw_art()                             # function starts



   
    
    
