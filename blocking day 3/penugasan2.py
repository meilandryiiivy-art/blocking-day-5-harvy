import turtle
t = turtle.Turtle()
t.speed(0)

# Persegi Panjang Merah
t.penup()
t.goto(-200, 100)
t.pendown()
t.color("red")
t.begin_fill()
for i in range(2):
    t.forward(120)
    t.right(90)
    t.forward(70)
    t.right(90)
t.end_fill()

# Segitiga Kuning
t.penup()
t.goto(0, 100)
t.pendown()
t.color("yellow")
t.begin_fill()
for i in range(3):
    t.forward(100)
    t.left(120)
t.end_fill()

# Trapesium Hijau
t.penup()
t.goto(200, 100)
t.pendown()
t.color("green")
t.begin_fill()
t.forward(120)
t.left(120)
t.forward(70)
t.left(60)
t.forward(70)
t.left(60)
t.forward(70)
t.end_fill()

# Jajar Genjang Biru
t.penup()
t.goto(-200, -100)
t.pendown()
t.color("blue")
t.begin_fill()
t.forward(120)
t.left(60)
t.forward(70)
t.left(120)
t.forward(120)
t.left(60)
t.forward(70)
t.end_fill()

# Segilima Ungu
t.penup()
t.goto(100, -100)
t.pendown()
t.color("purple")
t.begin_fill()
for i in range(5):
    t.forward(80)
    t.left(72)
t.end_fill()

turtle.done()