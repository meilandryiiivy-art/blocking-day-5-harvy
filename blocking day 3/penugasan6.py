import turtle

screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# ======================
# LINGKARAN LOGO
# ======================

# Ring luar abu
t.penup()
t.goto(0, -160)
t.pendown()
t.color("#d9d9d9")
t.begin_fill()
t.circle(160)
t.end_fill()

# Biru luar
t.penup()
t.goto(0, -145)
t.pendown()
t.color("#1f2f6b")
t.begin_fill()
t.circle(145)
t.end_fill()

# Ring putih
t.penup()
t.goto(0, -115)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(115)
t.end_fill()

# Biru dalam
t.penup()
t.goto(0, -95)
t.pendown()
t.color("#1f2f6b")
t.begin_fill()
t.circle(95)
t.end_fill()

# ======================
# TEKS
# ======================

t.penup()
t.goto(0, 125)
t.color("black")
t.write("SEKOLAH MENENGAH KEJURUAN",
        align="center",
        font=("Arial", 11, "bold"))

t.penup()
t.goto(0, -140)
t.write("PRESTASI PRIMA",
        align="center",
        font=("Arial", 13, "bold"))

# ======================
# BINTANG
# ======================

def star(x, y, size):
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()

t.color("black")
star(-120, 0, 20)
star(120, 0, 20)

# ======================
# IKON TANGAN (LEBIH MIRIP)
# ======================

# Outline putih
t.penup()
t.goto(-30, -60)
t.setheading(0)
t.color("white")
t.pendown()
t.begin_fill()

t.forward(60)      # bawah
t.left(90)
t.forward(50)
t.right(30)        # ibu jari miring
t.forward(20)
t.left(30)
t.forward(20)

# telunjuk panjang
t.left(90)
t.forward(80)
t.left(90)
t.forward(25)
t.left(90)
t.forward(80)

# sisi kiri
t.left(90)
t.forward(20)
t.left(30)
t.forward(20)
t.right(30)
t.forward(50)
t.left(90)
t.forward(60)

t.end_fill()

# Isi merah (lebih kecil agar ada border putih)
t.penup()
t.goto(-22, -50)
t.setheading(0)
t.color("red")
t.pendown()
t.begin_fill()

t.forward(44)
t.left(90)
t.forward(45)
t.right(30)
t.forward(15)
t.left(30)
t.forward(15)

t.left(90)
t.forward(70)
t.left(90)
t.forward(18)
t.left(90)
t.forward(70)

t.left(90)
t.forward(15)
t.left(30)
t.forward(15)
t.right(30)
t.forward(45)
t.left(90)
t.forward(44)

t.end_fill()

turtle.done()