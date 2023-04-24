import tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk
import csv

root = Tk()
root.geometry("1440x1440")
root.title("Assam")

def ScrolledFrame(parent):
    def on_resize(event):
        bbox = canvas.bbox('all')
        canvas.config(width=bbox[2], scrollregion=bbox)

    def on_mouse_wheel(event):
        canvas.yview_scroll(event.delta // -30, 'units')

    canvas = tkinter.Canvas(parent)

    canvas.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=1)

    sb = tkinter.Scrollbar(parent, orient=tkinter.VERTICAL, command=canvas.yview)

    sb.pack(side=tkinter.RIGHT, fill=tkinter.Y)



    canvas.config(yscrollcommand=sb.set)


    frame = tkinter.Frame(canvas)
    canvas.create_window(0, 0, window=frame, anchor='nw')
    frame.bind('<Configure>', on_resize)

    canvas.bind_all('<MouseWheel>', on_mouse_wheel)

    return frame


frame = ScrolledFrame(root)

with open("s3.csv", newline="") as file:
    reader = csv.reader(file)

    r = 0
    for col in reader:
        c = 0
        for row in col:
            label = tk.Label(frame, width=50, height=0, \
                             text=row, relief=tk.RIDGE)
            label.grid(row=r, column=c)
            c += 1
        r += 1

root.mainloop()
