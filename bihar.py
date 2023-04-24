import tkinter as tk
from tkinter import *
from tkinter import Tk
import os


root = Tk()
root.geometry("1440x1440")
root.config(bg="sky blue")
root.title("Bihar")

pic0 = PhotoImage(file='COVID.png')
labelphoto = Label(root, image = pic0, )
labelphoto.pack(pady=30)



pic = PhotoImage(file='STATS 2.png')
def open():
    top = Toplevel()
    top.geometry("1440x1440")
    top.iconbitmap(r'virus.ico')
    os.system('python biharst.py')
    top.destroy()

btn1 = Button(
    root,
    image=pic,
    bd=0,
    command=open
)
btn1.pack(pady=30)

pic1 = PhotoImage(file='GRAPH 2.png')
def open():
    top = Toplevel()
    top.geometry("1440x1440")
    top.iconbitmap(r'virus.ico')
    os.system('python bihargraph.py')
    top.destroy()

btn2 = Button(
    root,
    image=pic1,
    bd = 0,
    command=open
)
btn2.pack(pady=30)

pic3 = PhotoImage(file='HOSPITAL 2.png')
def open():
    top = Toplevel()
    top.geometry("1440x1440")
    top.iconbitmap(r'virus.ico')
    os.system('python biharhospital.py')
    top.destroy()

btn3 = Button(
    root,
    image=pic3,
    bd = 0,
    command=open
)
btn3.pack(pady=30)

pic4 = PhotoImage(file='Useful.png')
def open():
    top = Toplevel()
    top.geometry("1440x1440")
    top.iconbitmap(r'virus.ico')
    os.system('python biharlinks.py')
    top.destroy()

btn4 = Button(
    root,
    image=pic4,
    bd = 0,
    command=open
)
btn4.pack(pady=30)

btn = Button(root, text="Back", command=root.destroy, ).pack()

root.mainloop()
root.mainloop()