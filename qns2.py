from tkinter import *
top=Tk()
top.geometry=(400*250)
name=Label(top,text="NAME").place(x=30,y=50)
address=Label(top,text="address").place(x=30,y=90)
contact=Label(top,text="contact").place(x=30,y=130)
e1=Entry(top).place(x=80,y=50)
e2=Entry(top).place(x=80,y=90)
e3=Entry(top).place(x=95,y=135)
top.mainloop()

