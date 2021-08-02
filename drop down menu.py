from tkinter import*
root=Tk()
root.title('drop down menu')
root.iconbitmap('E:/images/global.ico')

def show():
    myLabel=Label(root,text=clicked.get()).pack()

clicked= StringVar()
clicked.set("monday")

drop=OptionMenu(root,clicked,"monday","tuesday","wednesday","thursday","friday")
drop.pack()

myButton=Button(root,text="show selection",command=show).pack()
mainloop()

