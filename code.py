import turtle
import tkinter as tk
t = turtle.Turtle()
t.speed('fastest')
t.shape('turtle')
t.home()

def draw_circle(radius, border_size, border_color, fill_color):
    t.fillcolor(fill_color)
    t.pensize(border_size)
    t.pencolor(border_color)
    t.penup()
    t.right(90)
    t.forward(radius)
    t.left(90)
    t.pendown()
    t.begin_fill()
    t.circle(radius)
    t.penup()
    t.home()
    t.end_fill()

def draw_squares(side, border_size, border_color, fill_color):
    t.fillcolor(fill_color)
    t.pensize(border_size)
    t.pencolor(border_color)
    t.begin_fill()
    for i in range(4):
        t.forward(side)
        t.left(90)
    t.end_fill()
    t.right(10)

def coconut_tree(x, y, trunk_height):
    trunk_width = 6
    t.penup()
    t.goto(x, y)
    t.setheading(90) 
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    for _ in range(2):
        t.forward(trunk_height)
        t.right(90)
        t.forward(trunk_width)
        t.right(90)
    t.end_fill()
    t.penup()
    t.setheading(90)
    t.goto(x + trunk_width/2, y + trunk_height)
    t.pendown()
    t.fillcolor("black")
    for angle in [60, 120, 180, 240, 300, 360]:
        t.begin_fill()
        t.setheading(angle)
        t.circle(18, 60)
        t.left(120)
        t.circle(18, 60)
        t.end_fill()

def pattern():
    t.pensize(3)
    angle = 10
    t.pencolor("#F19E74")
    t.pendown()
    for i in range(80):
        angle += 0.5
        t.forward(7)
        t.left(angle)
    t.home()

def but1():
    t.home()
    draw_circle(70, 0, "black", "#ED6F0F")
    t.home()
    t.fillcolor("black")
    t.pensize(2)
    t.begin_fill()
    t.left(180)
    t.forward(50)
    t.right(40)
    t.forward(20)
    t.left(160)
    t.forward(50)
    t.left(60)
    t.forward(80)
    t.left(60)
    t.forward(50)
    t.left(160)
    t.forward(20)
    t.home()
    t.end_fill()
    coconut_tree(-40, 0, 30) 
    coconut_tree(0, 0, 40)  
    coconut_tree(40, 0, 30)

def but2():
    t.home()
    draw_circle(70, 0, "black", "#AC2B79")
    for i in range(8):
        pattern()
        for j in range(i+1):
            t.left(360//8)

draw_circle(315, 2, "black", "#2E5D27")
for i in range(36):
    draw_squares(220, 1, "white", "#F6C209")
draw_circle(280, 2, "black", "#DD2DC5")
draw_circle(260, 2, "black", "#117226")
t.pencolor("black")
t.fillcolor("yellow")
for i in range(18):
    t.begin_fill()
    t.circle(300, 50)
    t.left(130)
    t.circle(300, 50)
    t.end_fill()
    t.left(270)
t.fillcolor("red")
for i in range(18):
    t.begin_fill()
    t.circle(280, 50)
    t.left(130)
    t.circle(280, 50)
    t.end_fill()
    t.left(270)
draw_circle(200, 0, "black", "#50E88D")
t.fillcolor("red")
t.pensize(2)
t.pencolor("black")
for i in range(24):
    t.begin_fill()
    t.circle(160, 75)
    t.left(180-75)
    t.circle(160, 75)
    t.end_fill()
draw_circle(140, 0, "black", "#F2F22E")
draw_circle(120, 0, "black", "#B5B504")
draw_circle(100, 0, "black", "#656500")
t.fillcolor("magenta")
t.pencolor("black")
for i in range(24):
    t.begin_fill()
    t.circle(80, 75)
    t.left(180-75)
    t.circle(80, 75)
    t.end_fill()
t.hideturtle()
screen = turtle.Screen()
canvas = screen.getcanvas()
root = canvas.winfo_toplevel()
frame = tk.Frame(root, bg="#fef3c7")
frame.pack(side=tk.BOTTOM, fill=tk.X)
label = tk.Label(
    frame,
    text="🌸 Happy Onam! Choose your preferred center design 🌸",
    font=("Helvetica", 16, "bold"),
    fg="#8b0000",
    bg="#fef3c7"
)
label.pack(side=tk.TOP, pady=10)

button_frame = tk.Frame(frame, bg="#fef3c7")
button_frame.pack(side=tk.TOP, pady=15)

btn_style = {
    "font": ("Helvetica", 12, "bold"),
    "fg": "white",
    "width": 12,
    "height": 2,
    "relief": tk.RAISED,
    "bd": 3
}
btn1 = tk.Button(button_frame, text="DESIGN 1", bg="#2e8b57", **btn_style, command=but1) 
btn1.pack(side=tk.LEFT, padx=20)
btn2 = tk.Button(button_frame, text="DESIGN 2", bg="#6a5acd", **btn_style, command=but2)
btn2.pack(side=tk.LEFT, padx=20)
screen.mainloop()
