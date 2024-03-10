from tkinter import *
from tkinter import ttk
from tkinter import filedialog
#Create an instance of Tkinter frame
win= Tk()
#Define the geometry
win.geometry("750x250")
def select_file():
   path= filedialog.askdirectory(title="Select a File")
   Label(win, text=path, font=13).pack()
#Create a label and a Button to Open the dialog
Label(win, text="Click the Button to Select a File", font=('Aerial 18 bold')).pack(pady=20)
button= ttk.Button(win, text="Select", command= select_file)
button.pack(ipadx=5, pady=15)
win.mainloop()