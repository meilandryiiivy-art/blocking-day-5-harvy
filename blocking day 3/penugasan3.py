import turtle

# ======================
# Setup layar
# ======================
screen = turtle.Screen()
screen.title("Bendera Indonesia")
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# ======================
# Fungsi menggambar persegi panjang berwarna
# ======================
def draw_rectangle(x, y, width, height, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()

# ======================
# Ukuran bendera
# ======================
bendera_width = 400
bendera_height = 260  # proporsi 2:3

# Koordinat pojok kiri atas bendera
start_x = -bendera_width / 2
start_y = bendera_height / 2

# ======================
# Bagian Merah
# ======================
draw_rectangle(start_x, start_y, bendera_width, bendera_height / 2, "red")

# ======================
# Bagian Putih
# ======================
draw_rectangle(start_x, start_y - bendera_height / 2, bendera_width, bendera_height / 2, "white")

# ======================
# Bingkai hitam tipis (opsional)
# ======================
t.penup()
t.goto(start_x, start_y)
t.pendown()
t.pensize(2)
t.color("black")
for _ in range(2):
    t.forward(bendera_width)
    t.right(90)
    t.forward(bendera_height)
    t.right(90)

# ======================
# Selesai
# ======================
turtle.done()