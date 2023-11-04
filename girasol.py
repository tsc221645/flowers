import turtle as t

def petalo1():
    t.color("yellow")
    t.fillcolor("yellow")
    t.width(3)
    t.pendown()
    t.begin_fill()
    t.circle(100, 100)
    t.left(80)
    t.circle(100, 100)
    t.end_fill()

petalo1()