import tkinter
from tkinter import filedialog
from tkinter import *
root = Tk()
# root.withdraw()
folder_selected =''
def openfile():
    folder_selected = filedialog.askdirectory()
    label.config(text=folder_selected)

button = Button(root, text="open", command=openfile)
button.grid(row=0,column=0)
label = Label(root, text=folder_selected,font=18)
label.grid(row=0,column=1)
root.mainloop()