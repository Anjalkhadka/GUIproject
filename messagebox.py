from tkinter import*
from PIL import Image Tk,Image

root=Tk()
root.title=('messagebox')
root.iconbitmap('app-icons-twitter.png')
def popup():
    Messagebox.showninfo("This is my pop","Hello nepal")
Button(root, text="popup",command=open).pack()
mainloop()