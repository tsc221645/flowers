import turtle as t
t.speed(1)
def petalo():
    t.width(3)
    t.fillcolor("#cd8efa")
    t.color("#a241e8")
    t.pendown()
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    t.penup()

def tallo(startingX, startingY):
    t.penup()
    t.goto(startingX, startingY+150)
    t.width(5)
    t.color("#2b9c27")
    t.right(90)
    t.pendown()
    t.forward(350)
    t.penup()

def dibujarLavanda(startingX, startingY):
    tallo(startingX, startingY)

dibujarLavanda(0,0)
