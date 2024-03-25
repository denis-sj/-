import tkinter as tk
from tkinter import ttk
from math import cos, sin, radians
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Расчёт первой и второй космической скорости")

w = root.winfo_screenwidth()
h = root.winfo_screenheight()
root.geometry(f'{w}x{h}')
root.minsize(1280,720)
root.maxsize(w,h)

def calculate_velocity(r):
    G = 6.67 * (10 ** -11)
    M = 5.97 * (10 ** 24)
    v1 = ((G * M) / r) ** 0.5
    v2 = ((2 * G * M) / r) ** 0.5
    return v1, v2

def update_velocity(event):
    r = trajectory_slider.get()
    v1, v2 = calculate_velocity(r)
    velocity_label.config(text="Первая космическая скорость: {} м/с\nВторая космическая скорость: {} м/с".format(round(v1, 2), round(v2, 2)))

but1 = 0
def show_text():
    global but1
    if but1 == 0:
        lbl1 = Label(root, text = "Первая космическая скорость — это скорость, с которой надо горизонтально запустить объект, чтобы он стал вращаться вокруг Земли по круговой орбите.")
        formula1 = Label(root, text = "Формула: v₁ = √GM/R")
        lbl2 = Label(root, text = "Вторая космическая скорость — это наименьшая скорость, которую необходимо придать космическому аппарату для преодоления притяжения планеты и покидания замкнутой орбиты вокруг неё.")
        formula2 = Label(root, text = "Формула: v₂ = √2GM/R")
        lbl1.place(relx = 0.3, rely = 0.55)
        formula1.place(relx = 0.47, rely = 0.57)
        lbl2.place(relx = 0.24, rely = 0.59)
        formula2.place(relx = 0.47, rely = 0.61)
        but1 += 1

# information
but = Button(root, text = "Information", command = show_text, font = 'Arial 20')
but.place(relx = 0.6, rely = 0.492)

def move_object():
    global current_angle
    current_angle = (current_angle + 1) % 360 
    radius = 66.7 + (trajectory_slider.get() - 150) / 356.36

    x = 500 + radius * cos(radians(current_angle)) 
    y = 690 + radius * sin(radians(current_angle)) 
    canvas.coords(orbiting_object, x-10, y-10, x+10, y+10) 


# planeti
canvas = tk.Canvas(root, width=1000, height=1000)
canvas.place(relx=0.5009, rely=0.5, anchor="s")

ball = canvas.create_oval(540, 735, 460, 655, fill="blue")

orbiting_object = canvas.create_oval(140, 140, 150, 150, fill="green")

# radius
radius_label = Label(root, text="Радиус:")
radius_label.place(relx = 0.489, rely = 0.43)

# ползунок
trajectory_slider = tk.Scale(root, from_=150, to=35786, orient="horizontal", length=1000, command=update_velocity)
trajectory_slider.place(relx = 0.25, rely = 0.45)
# text
velocity_label = Label(root, text="Первая космическая скорость: 0 м/с\nВторая космическая скорость: 0 м/с")
velocity_label.place(relx = 0.44, rely = 0.5)

current_angle = 0  

def speed_control():
    global speed
    speed = round((trajectory_slider.get() - 150) * 0.002665844 + 5)


def update_position():
    move_object()
    speed_control()
    root.after(speed, update_position)


update_position()


root.mainloop()
