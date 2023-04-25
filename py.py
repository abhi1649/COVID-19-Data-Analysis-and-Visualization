import tkinter as tk
from tkinter import *
from tkinter import Tk
import os


root = Tk()
root.geometry("1440x1440")
root.config(bg="sky blue")

pic0 = PhotoImage(file='COVID.png')
labelphoto = Label(root, image = pic0, )
labelphoto.pack(pady=30)



pic = PhotoImage(file='STATS 2.png')
def open():
    top = Toplevel()
    top.geometry("1440x1440")
    top.iconbitmap(r'virus.ico')
    os.system('python stats.py')
    top.destroy()

btn1 = Button(
    root,
    image=pic,
    border=0,
    command=open


)
btn1.pack(pady=30)

pic1 = PhotoImage(file='GRAPH 2.png')
btn2 = Button(
    root,
    image=pic1,
    bd = 0,

)
btn2.pack(pady=30)

pic3 = PhotoImage(file='HOSPITAL 2.png')
btn3 = Button(
    root,
    image=pic3,
    bd = 0,


)
btn3.pack(pady=30)

pic4 = PhotoImage(file='DATA 2.png')
btn4 = Button(
    root,
    image=pic4,
    bd = 0,

)
btn4.pack(pady=30)
btn = Button(root, text="Back", command=root.destroy, ).pack()
root.mainloop()
root.mainloop()