import turtle as t
t.speed(20)
def petalo1():
    t.color("#ffec24")
    t.fillcolor("#f7ff69")
    t.width(3)
    t.pendown()
    t.begin_fill()
    t.circle(50, 100)
    t.left(80)
    t.circle(50, 100)
    t.end_fill()
    
def petalo2():
    t.color("#f8ff24")
    t.fillcolor("#f8ff24")
    t.width(3)
    t.pendown()
    t.begin_fill()
    t.circle(80, 100)
    t.left(80)
    t.circle(80, 100)
    t.end_fill()

def petalo3():
    t.color("#ffec24")
    t.fillcolor("#ffec24")
    t.width(3)
    t.pendown()
    t.begin_fill()
    t.circle(100, 100)
    t.left(80)
    t.circle(100, 100)
    t.end_fill()

for i in range(0,13):
    t.right(30)
    petalo3()

for i in range(0,13):
    t.right(30)
    petalo2()

for i in range(0,13):
    t.right(30)
    petalo1()

