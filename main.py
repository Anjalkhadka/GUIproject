from tkinter import *
root =Tk ()
Button1=Button(root, text="LEFT", fg="green")
Button1.pack(side=LEFT)
Button2=Button(root, text="RIGHT", fg="black")
Button2.pack(side=RIGHT)
Button3=Button(root, text="TOP", fg="yellow")
Button3.pack(side=TOP)
root.mainloop()