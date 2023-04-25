import tkinter as tk
from tkinter import *
from tkinter import Tk


root = Tk()



whateve_you_do = "\n COVID -19 TRACKER \n"

msg0 = tk.Message(root, text=whateve_you_do)
msg0.config(font=('Helvetica', 60, 'italic', 'bold'), anchor="n", justify=LEFT)

msg0.pack()
whatever_you_do = " \n1. STATS (TABLE)"
msg1 = tk.Message(root, text=whatever_you_do)
msg1.config(font=('Helvetica', 40, 'italic'), anchor='n', justify=LEFT)
msg1.pack()

whatev_you_do = "\n2. GRAPH"
msg2 = tk.Message(root, text=whatev_you_do)
msg2.config(font=('Helvetica', 40, 'italic'), anchor='n', justify=LEFT)
msg2.pack()

whate_you_do = "\n3. HOSPITALS AND TESTING LAB INFO. "
msg3 = tk.Message(root, text=whate_you_do)
msg3.config(font=('Helvetica', 40, 'italic'), anchor='n', justify=LEFT)
msg3.pack()

what_you_do = "\n 4. DATA FOR CAPITAL CITY."
msg4 = tk.Message(root, text=what_you_do)
msg4.config(font=('Helvetica', 40, 'italic'), anchor='n', justify=LEFT)
msg4.pack()


root.mainloop()
root.mainloop()