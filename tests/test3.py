from tkinter import *
from tkinter import ttk
from tkinter import filedialog
gui = Tk()
gui.geometry("400x400")
gui.title("FC")

def getFolderPath():
    folder_selected = filedialog.askdirectory()
    folderPath.set(folder_selected)

def doStuff():
    folder = folderPath.get()
    print("Doing stuff with folder", folder)

folderPath = StringVar()
a = Label(gui ,text="Enter name")
a.grid(row=0,column = 0)
E = Entry(gui,textvariable=folderPath)
E.grid(row=0,column=1)
btnFind = ttk.Button(gui, text="Browse Folder",command=getFolderPath)
btnFind.grid(row=0,column=2)

c = ttk.Button(gui ,text="find", command=doStuff)
c.grid(row=4,column=0)
gui.mainloop()