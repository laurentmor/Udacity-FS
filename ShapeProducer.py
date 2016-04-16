import turtle
pen=turtle.Turtle()
screen=turtle.Screen()
def create():
    pen.shape("turtle")
    pen.color("blue")
    screen.setup(1800,1600)
    #screen.bgcolor("red")
    

def drawLine():
    pen.forward(100)
    pen.right(90)
    
def drawSquare():
    
    for i in range(0,4):
         drawLine()
         


def drawFlower():
    for i in range(0,36):
        drawSquare()
        pen.right(10)
        
def run():
    create()
    drawFlower()
    pen.up()
    pen.backward(250)
    pen.down()
    drawFlower()
    

    
        


run()    
screen.exitonclick()
