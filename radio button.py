from tkinter import*
root=Tk()
HOTEL=[
    ("Momo","Momo"),
    ("cheese","cheese"),
    ("Mushroom","Mushroom"),
    ("Pizza","Pizza")

]
Food=StringVar()
Food.set("Momo")

for text, hotel in HOTEL:
    Radiobutton(root, text=text, variable=Food, value=hotel)
def clicked(value):
    myLabel=Label(root,text=value)
    myLabel.pack()


myButton=Button(root,text="click",command=lambda:clicked(Food.get())).pack()
root.mainloop()

