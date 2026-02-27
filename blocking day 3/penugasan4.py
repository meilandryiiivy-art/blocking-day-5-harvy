import turtle
t = turtle.Turtle()
t.speed(0)
t.left(90)

def fibonacci_tree(panjang, level):
    if level == 0:
        return
    t.forward(panjang)
    t.left(30)
    fibonacci_tree(panjang * 0.7, level - 1)
    t.right(60)
    fibonacci_tree(panjang * 0.7, level - 1)
    t.left(30)
    t.backward(panjang)

t.penup()
t.goto(0, -200)
t.pendown()
t.color("brown")

fibonacci_tree(80, 6)

turtle.done()