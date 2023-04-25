import tkinter as tk
from tkinter import *
import os
from tkinter import ttk


root = Tk()
root.geometry("1440x1440")
root.title("COVID-19 TRACKER")
root.iconbitmap(r'virus.ico')



main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

my_canvas = Canvas(main_frame)
my_canvas.configure(background ="sky blue" )

my_canvas.pack(side=LEFT,fill=BOTH, expand=1)

my_scrollbar= ttk.Scrollbar(main_frame, orient= VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>',lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

head1 = PhotoImage(file='mainwin.png')
labelphoto = Label(main_frame, image = head1, )
labelphoto.pack()

second_frame = Frame(my_canvas)
second_frame.configure(background = "sky blue")
my_canvas.create_window((0,0),window=second_frame, anchor="nw")




head = PhotoImage(file='heading.png')
labelphoto = Label(second_frame, image = head, )
labelphoto.pack()

paru = PhotoImage(file='arunachal.png')


def open():
    top = Toplevel()
    top.geometry("1440x1440")
    top.title('Arunachal Pradesh')
    top.iconbitmap(r'virus.ico')
    os.system('python arunachal.py')
    top.destroy()

btn15 = Button(
    second_frame,
    image=paru,
    bd = 0,
    text="Arunachal Pradesh",
    compound=TOP,
    command=open,
)
btn15.pack(pady=30)


pit = PhotoImage(file='Ap.png')
def open():
    top = Toplevel()
    top.geometry("1440x1440")
    top.title('Andhra Pradesh')
    top.iconbitmap(r'virus.ico')
    os.system('python andhra.py')
    top.destroy()


btn16 = Button(
    second_frame,
    image=pit,
    border=0,
    text="Andhra Pradesh",
    compound=TOP,
    command=open,
)
btn16.pack(pady=30)

phoc = PhotoImage(file='Assam.png')
def open():
    top = Toplevel()
    top.geometry("1440x1440")
    top.title('Assam')
    top.iconbitmap(r'virus.ico')
    os.system('python assam.py')
    top.destroy()
    

btn18 = Button(
    second_frame,
    image=phoc,
    border=0,
    text="Assam",
    compound=TOP,
    command=open,
)
btn18.pack(pady=30)

pbirh = PhotoImage(file='bh.png')
def open():
    top = Toplevel()
    top.geometry("1440x1440")
    top.title('BIHAR')
    top.iconbitmap(r'virus.ico')
    os.system('python bihar.py')
    top.destroy()
    
btn5 = Button(
    second_frame,
    image=pbirh,
    border=0,
    text="BIHAR",
    compound=TOP,
    command=open,
)
btn5.pack(pady=30)


phocp = PhotoImage(file='chattisgarh.png')
def open():
    top = Toplevel()
    top.geometry("1440x1440")
    top.title('Chattisgarh')
    top.iconbitmap(r'virus.ico')
    os.system('python chhattisgarh.py')
    top.destroy()


btn20 = Button(
    second_frame,
    image=phocp,
    border=0,
    text="Chattisgarh",
    compound=TOP,
    command=open,
)
btn20.pack(pady=30)

photo = PhotoImage(file='delhi.png')
def open():
    top = Toplevel()
    top.geometry("1440x1440")
    top.title('DELHI')
    top.iconbitmap(r'virus.ico')
    os.system('python delhi.py')
    top.destroy()
    btn6 = Button(top, text="Back",  ).pack()


btn1 = Button(
    second_frame, image=photo, borderwidth=0, text="Delhi", compound=TOP, command=open).pack()

phocw = PhotoImage(file='goa.png')
def open():
    top = Toplevel()
    top.geometry("1440x1440")
    top.title('Goa')
    top.iconbitmap(r'virus.ico')
    os.system('python goa.py')
    top.destroy()


btn22 = Button(
    second_frame,
    image=phocw,
    border=0,
    text="Goa",
    compound=TOP,
    command=open,
)
btn22.pack(pady=30)

phoci = PhotoImage(file='gujarat.png')
def open():
    top = Toplevel()
    top.geometry("1440x1440")
    top.title('Gujarat')
    top.iconbitmap(r'virus.ico')
    os.system('python gujarat.py')
    top.destroy()

btn24 = Button(
    second_frame,
    image=phoci,
    border=0,
    text="Gujarat",
    compound=TOP,
    command=open,
)
btn24.pack(pady=30)

phocu = PhotoImage(file='haryana.png')
def open():
    top = Toplevel()
    top.geometry("1440x1440")
    top.title('Haryana')
    top.iconbitmap(r'virus.ico')
    os.system('python haryana.py')
    top.destroy()

btn26 = Button(
    second_frame,
    image=phocu,
    border=0,
    text="Haryana",
    compound=TOP,
    command=open,
)
btn26.pack(pady=30)

phocq = PhotoImage(file='jharkhand.png')
def open():
    top = Toplevel()
    top.geometry("1440x1440")
    top.title('Jharkhand')
    top.iconbitmap(r'virus.ico')
    os.system('python jharkhand.py')
    top.destroy()

btn28 = Button(
    second_frame,
    image=phocq,
    border=0,
    text="Jharkhand",
    compound=TOP,
    command=open,
)
btn28.pack(pady=30)

phocqq = PhotoImage(file='karnatka.png')
def open():
    top = Toplevel()
    top.geometry("1440x1440")
    top.title('Karnataka')
    top.iconbitmap(r'virus.ico')
    os.system('python karnataka.py')
    top.destroy()

btn30 = Button(
    second_frame,
    image=phocqq,
    border=0,
    text="Karnataka",
    compound=TOP,
    command=open,
)
btn30.pack(pady=30)

phoww = PhotoImage(file='himachal.png')
def open():
    top = Toplevel()
    top.geometry("1440x1440")
    top.title('Himachal')
    top.iconbitmap(r'virus.ico')
    os.system('python himachal.py')
    top.destroy()

btn32 = Button(
    second_frame,
    image=phoww,
    border=0,
    text="Himachal",
    compound=TOP,
    command=open,
)
btn32.pack(pady=30)

phoee = PhotoImage(file='kerela.png')
def open():
    top = Toplevel()
    top.geometry("1440x1440")
    top.title('kerala')
    top.iconbitmap(r'virus.ico')
    os.system('python kerala.py')
    top.destroy()

btn34 = Button(
    second_frame,
    image=phoee,
    border=0,
    text="kerala",
    compound=TOP,
    command=open,
)
btn34.pack(pady=30)

phorr = PhotoImage(file='madhya.png')
def open():
    top = Toplevel()
    top.geometry("1440x1440")
    top.title('Madhya Pradesh')
    top.iconbitmap(r'virus.ico')
    os.system('python madhya.py')
    top.destroy()

btn36 = Button(
    second_frame,
    image=phorr,
    border=0,
    text="Madhya Pradesh",
    compound=TOP,
    command=open,
)
btn36.pack(pady=30)

phott = PhotoImage(file='maharashtra.png')
def open():
    top = Toplevel()
    top.geometry("1440x1440")
    top.title('Maharashtra')
    top.iconbitmap(r'virus.ico')
    os.system('python maharashtra.py')
    top.destroy()

btn38 = Button(
    second_frame,
    image=phott,
    border=0,
    text="Maharashtra",
    compound=TOP,
    command=open,
)
btn38.pack(pady=30)

phoyy = PhotoImage(file='manipur.png')
def open():
    top = Toplevel()
    top.geometry("1440x1440")
    top.title('Manipur')
    top.iconbitmap(r'virus.ico')
    os.system('python manipur.py')
    top.destroy()

btn40 = Button(
    second_frame,
    image=phoyy,
    border=0,
    text="Manipur",
    compound=TOP,
    command=open,
)
btn40.pack(pady=30)

phouu = PhotoImage(file='meghalya.png')
def open():
    top = Toplevel()
    top.geometry("1440x1440")
    top.title('Meghalaya')
    top.iconbitmap(r'virus.ico')
    os.system('python meghalaya.py')
    top.destroy()

btn42 = Button(
    second_frame,
    image=phouu,
    border=0,
    text="Meghalaya",
    compound=TOP,
    command=open,
)
btn42.pack(pady=30)

phoii = PhotoImage(file='mizoram.png')
def open():
    top = Toplevel()
    top.geometry("1440x1440")
    top.title('Mizoram')
    top.iconbitmap(r'virus.ico')
    os.system('python mizoram.py')
    top.destroy()

btn44 = Button(
    second_frame,
    image=phoii,
    border=0,
    text="Mizoram",
    compound=TOP,
    command=open,
)
btn44.pack(pady=30)

phooo = PhotoImage(file='nagaland.png')
def open():
    top = Toplevel()
    top.geometry("1440x1440")
    top.title('Nagaland')
    top.iconbitmap(r'virus.ico')
    os.system('python nagaland.py')
    top.destroy()

btn46 = Button(
    second_frame,
    image=phooo,
    border=0,
    text="Nagaland",
    compound=TOP,
    command=open,
)
btn46.pack(pady=30)

phopp = PhotoImage(file='odisha.png')
def open():
    top = Toplevel()
    top.geometry("1440x1440")
    top.title('Odisha')
    top.iconbitmap(r'virus.ico')
    os.system('python odisha.py')
    top.destroy()

btn47 = Button(
    second_frame,
    image=phopp,
    border=0,
    text="Odisha",
    compound=TOP,
    command=open,
)
btn47.pack(pady=30)

phoaa = PhotoImage(file='punjab.png')
def open():
    top = Toplevel()
    top.geometry("1440x1440")
    top.title('Punjab')
    top.iconbitmap(r'virus.ico')
    os.system('python punjab.py')
    top.destroy()

btn49 = Button(
    second_frame,
    image=phoaa,
    border=0,
    text="Punjab",
    compound=TOP,
    command=open,
)
btn49.pack(pady=30)

pbrh = PhotoImage(file='raj.png')
def open():
    top = Toplevel()
    top.geometry("1440x1440")
    top.title('RAJASTHAN')
    top.iconbitmap(r'virus.ico')
    os.system('python rajasthan.py')
    top.destroy()



btn4 = Button(
    second_frame,
    image=pbrh,
    border=0,
    text="RAJASTHAN",
    compound=TOP,
    command=open,
)
btn4.pack(pady=30)

phoss = PhotoImage(file='sikkim.png')
def open():
    top = Toplevel()
    top.geometry("1440x1440")
    top.title('Sikkim')
    top.iconbitmap(r'virus.ico')
    os.system('python sikkim.py')
    top.destroy()

btn51 = Button(
    second_frame,
    image=phoss,
    border=0,
    text="Sikkim",
    compound=TOP,
    command=open,
)
btn51.pack(pady=30)

phodd = PhotoImage(file='tamilnadu.png')
def open():
    top = Toplevel()
    top.geometry("1440x1440")
    top.title('Tamil Nadu')
    top.iconbitmap(r'virus.ico')
    os.system('python tamil.py')
    top.destroy()

btn53 = Button(
    second_frame,
    image=phodd,
    border=0,
    text="Tamil Nadu",
    compound=TOP,
    command=open,
)
btn53.pack(pady=30)

phoff = PhotoImage(file='telengana.png')
def open():
    top = Toplevel()
    top.geometry("1440x1440")
    top.title('Telengana')
    top.iconbitmap(r'virus.ico')
    os.system('python telangana.py')
    top.destroy()

btn56 = Button(
    second_frame,
    image=phoff,
    border=0,
    text="Telengana",
    compound=TOP,
    command=open,
)
btn56.pack(pady=30)

phogg = PhotoImage(file='tripura.png')
def open():
    top = Toplevel()
    top.geometry("1440x1440")
    top.title('Tripura')
    top.iconbitmap(r'virus.ico')
    os.system('python tripura.py')
    top.destroy()

btn58 = Button(
    second_frame,
    image=phogg,
    border=0,
    text="Tripura",
    compound=TOP,
    command=open,
)
btn58.pack(pady=30)

ph = PhotoImage(file='up.png')
def open():
    top = Toplevel()
    top.geometry("1440x1440")
    top.title('UTTAR PRADESH')
    top.iconbitmap(r'virus.ico')
    os.system('python up.py')
    top.destroy()

btn2 = Button(
    second_frame,
    image=ph,
    border=0,
    text="UTTAR PRADESH",
    compound=TOP,
    command=open,
)
btn2.pack(pady=30)

pbukh = PhotoImage(file='bih.png')
def open():
    top = Toplevel()
    top.geometry("1440x1440")
    top.title('UTTRAKHAND')
    top.iconbitmap(r'virus.ico')
    os.system('python uttarakhand.py')
    top.destroy()

btn3 = Button(
    second_frame,
    image=pbukh,
    border=0,
    text="UTTRAKHAND",
    compound=TOP,
    command=open,
)
btn3.pack(pady=30)

phohh = PhotoImage(file='westbwngal.png')
def open():
    top = Toplevel()
    top.geometry("1440x1440")
    top.title('West Bengal')
    top.iconbitmap(r'virus.ico')
    os.system('python west bengal.py')
    top.destroy()

btn60 = Button(
    second_frame,
    image=phohh,
    border=0,
    text="West Bengal",
    compound=TOP,
    command=open,
)
btn60.pack(pady=30)

phojj = PhotoImage(file='andaman.png')
def open():
    top = Toplevel()
    top.geometry("1440x1440")
    top.title('Andaman Nicobar')
    top.iconbitmap(r'virus.ico')
    os.system('python andaman.py')
    top.destroy()

btn62 = Button(
    second_frame,
    image=phojj,
    border=0,
    text="Andaman Nicobar",
    compound=TOP,
    command=open,
)
btn62.pack(pady=30)

phokk = PhotoImage(file='chandigarh.png')
def open():
    top = Toplevel()
    top.geometry("1440x1440")
    top.title('Chandigarh')
    top.iconbitmap(r'virus.ico')
    os.system('python chandigarh.py')
    top.destroy()

btn64 = Button(
    second_frame,
    image=phokk,
    border=0,
    text="Chandigarh",
    compound=TOP,
    command=open,
)
btn64.pack(pady=30)

pholl = PhotoImage(file='dadar and nagar and diu.png')
def open():
    top = Toplevel()
    top.geometry("1440x1440")
    top.title('Daman & Diu Dadar & nagar')
    top.iconbitmap(r'virus.ico')
    os.system('python dadra.py')
    top.destroy()

btn66 = Button(
    second_frame,
    image=pholl,
    border=0,
    text="Daman & Diu Dadar & nagar",
    compound=TOP,
    command=open,
)
btn66.pack(pady=30)

phozz = PhotoImage(file='jnk.png')
def open():
    top = Toplevel()
    top.geometry("1440x1440")
    top.title('Jammu & Kashmir')
    top.iconbitmap(r'virus.ico')
    os.system('python jammu.py')
    top.destroy()

btn68 = Button(
    second_frame,
    image=phozz,
    border=0,
    text="Jammu & Kashmir",
    compound=TOP,
    command=open,
)
btn68.pack(pady=30)

phoxx = PhotoImage(file='laddakh.png')
def open():
    top = Toplevel()
    top.geometry("1440x1440")
    top.title('Ladakh')
    top.iconbitmap(r'virus.ico')
    os.system('python ladakh.py')
    top.destroy()

btn70 = Button(
    second_frame,
    image=phoxx,
    border=0,
    text="Ladakh",
    compound=TOP,
    command=open,
)
btn70.pack(pady=30)

phocc = PhotoImage(file='lakshdweep.png')
def open():
    top = Toplevel()
    top.geometry("1440x1440")
    top.title('Lakshadweep')
    top.iconbitmap(r'virus.ico')
    os.system('python lakshadweep.py')
    top.destroy()

btn72 = Button(
    second_frame,
    image=phocc,
    border=0,
    text="Lakshadweep",
    compound=TOP,
    command=open,
)
btn72.pack(pady=30)

phovv = PhotoImage(file='pudduchery.png')
def open():
    top = Toplevel()
    top.geometry("1440x1440")
    top.title('Puducherry')
    top.iconbitmap(r'virus.ico')
    os.system('python puducherry.py')
    top.destroy()

btn74 = Button(
    second_frame,
    image=phovv,
    border=0,
    text="Puducherry",
    compound=TOP,
    command=open,
)
btn74.pack(pady=30)



btn = Button(root, text="Back", command=root.destroy, ).pack()



root.mainloop()

root.mainloop()

