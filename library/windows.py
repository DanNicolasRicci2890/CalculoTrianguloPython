from tkinter import *

def ventanaroot(root):
    root.title("Triangulo")
    root.maxsize(width=1000, height=400)
    root.minsize(width=1000, height=400)
    root.config(background="#BEBFB2")
    
def CrearTextBox(root, texto, valor, w, h, px, py):
    frame = crearframe(root, w, h, px, py)
    crearlabel(frame, texto, 10, 13)
    crearentry(frame, valor, 100, 2)
    
def crearframe(root, w, h, px, py):
    frame = Frame(root)
    frame.place(width=w, height=h, x=px, y=py)
    return frame

def crearlabel(frame, texto, px, py):
    label = Label(frame, text=texto)
    label.config(font=("Consoles", 16, "bold", "italic"))
    label.place(x=px, y=px)
    
def crearentry(frame, valor, px, py):
    entryA = Entry(frame, justify="left", textvariable=valor)
    entryA.config(width=10, font=("Arial", 26, "bold", "italic"), foreground="blue")
    entryA.place(x=px, y=py)