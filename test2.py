import turtle
def draw_circle():
    window = turtle.Screen()
    window.bgcolor("black")
    brad = turtle.Turtle()
    brad.shape("arrow")
    brad.color("green")
# for alphabet M
    brad.seth(90)
    brad.forward(100)
    brad.right(130)
    brad.forward(90)
    brad.left(90)
    brad.forward(80)
    brad.right(140)
    brad.forward(100)
# for alphabet E
    brad.pu()
    brad.setpos(130,0)
    brad.pd()
    brad.seth(0)
    brad.left(90)
    brad.forward(100)
    brad.back(100)
    brad.forward(100)
    brad.right(90)
    brad.forward(70)
    brad.back(70)
    brad.right(90)
    brad.pu()
    brad.forward(50)
    brad.pd()
    brad.left(90)
    brad.forward(70)
    brad.pu()
    brad.right(90)
    brad.forward(50)
    brad.pd()
    brad.right(90)
    brad.forward(60)
   
    
    
    window.exitonclick()
 
draw_circle()

#brad.right(90)
 #   brad.forward(100)
