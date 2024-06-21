#Program grafika s pouzitim n-tic pre suradnice bodov
import tkinter
a = (70, 150)
b = (200, 200)
c = (150, 250)
d = (120, 70)
e = (50, 220)
canvas = tkinter.Canvas()
canvas.pack()
canvas.create_polygon(e, a, c, fill='green')
canvas.create_polygon(e, d, b, fill='yellow')
canvas.create_polygon(a, b, c, d, fill='red')
canvas.create_polygon(a, c, d, b, fill='blue')
