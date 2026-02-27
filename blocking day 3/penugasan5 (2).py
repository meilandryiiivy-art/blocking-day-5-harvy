import turtle

#Inisialisasi turtle
t = turtle.Turtle()
t.shape("turtle")
t.color("gold")
t.pensize(3)

#logika menggambar bintang
#sudut luar bintang berujung lima adalah 144 derajat
for i in range(5):
    t.forward(200) #panjang garis
    t.right(144)   #sudut belok

#menjaga jendela tetap terbuka 
turtle.done()