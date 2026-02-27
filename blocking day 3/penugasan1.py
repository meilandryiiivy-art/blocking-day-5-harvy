import turtle

t = turtle.Turtle()
t.speed(0)

# =========================
# 1. Bangun datar
# =========================
t.penup()
t.goto(-300, 200)
t.pendown()

# Persegi Panjang
for i in range(2):
    t.forward(100)
    t.right(90)
    t.forward(60)
    t.right(90)

# Segitiga
t.penup()
t.goto(-150, 200)
t.pendown()
for i in range(3):
    t.forward(80)
    t.left(120)

# Trapesium
t.penup()
t.goto(0, 200)
t.pendown()
t.forward(100)
t.left(120)
t.forward(60)
t.left(60)
t.forward(60)
t.left(60)
t.forward(60)

# Jajar Genjang
t.penup()
t.goto(150, 200)
t.pendown()
t.forward(100)
t.left(60)
t.forward(60)
t.left(120)
t.forward(100)
t.left(60)
t.forward(60)

# Belah Ketupat
t.penup()
t.goto(300, 200)
t.pendown()
for i in range(4):
    t.forward(70)
    t.left(60)
    t.forward(70)
    t.left(120)