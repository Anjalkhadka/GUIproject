from tkinter import*
root=Tk()
root.title('frame')
frame = LabelFrame(root, text="My frame", padx=50, pady=50)
frame.pack(padx=10, pady=10)


button1=Button(frame, text="Click this")
button1.grid(row=0,column=0)
button2=Button(frame, text="anjal")
button2.grid(row=1,column=1)

root.mainloop()

