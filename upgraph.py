from tkinter import *
from tkinter.ttk import *

import matplotlib.pyplot as plt
import pandas as pd

master = Tk()

master.geometry("2000x2000")
master.configure(bg='deep sky blue')
master.title("Uttar Pradesh")

def openNewWindow():
    newWindow = Toplevel(master)

    Label(newWindow,
          text="").pack()
    plt.style.use('bmh')
    df = pd.read_csv('uttar pradesh.csv')

    x = df['Day']
    y = df['Confirmed']

    plt.xlabel('Day', fontsize=20)
    plt.ylabel('Confirmed', fontsize=20)
    plt.bar(x, y)
    plt.show()


def openNewWindow1():
    newWindow = Toplevel(master)

    Label(newWindow,
          text="").pack()
    plt.style.use('bmh')
    df = pd.read_csv('uttar pradesh.csv')

    x = df['Day']
    y = df['Confirmed']

    plt.xlabel('Day', fontsize=20)
    plt.ylabel('Confirmed', fontsize=20)
    plt.scatter(x, y)
    plt.show()


label = Label(master,
              text="GRAPHICAL DATA", font=("Times New Roman", 60))

label.pack(pady=10)

photo = PhotoImage(file=r"gr.png")
photoimage = photo.subsample(4, 6)

Button(master, image=photoimage,
       compound=LEFT).pack(side=TOP)


btn = Button(master,
             text="BAR GRAPH",
             command=openNewWindow)
btn.pack(pady=10)

btn = Button(master, text="SCATTER GRAPH",
             command=openNewWindow1)

btn.pack(pady=10)
btn = Button(master, text="Back", command=master.destroy, ).pack()
master.mainloop()
mainloop()