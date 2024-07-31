# ======================== Importing Libraries ========================
import os                       # For interacting with the operating system.
import shutil                   # To move files.
from tkinter import *           # To make GUI.
from tkinter import filedialog  # To open file directories.
import customtkinter        # For better GUI.
# ======================================================================


# =============================== Window ===============================
window = Tk()                   # Creating an instance of Tkinter frame.
window.title("File Organizer")  # Window name.

icon = PhotoImage(file='icon.png')
window.iconphoto(False, icon)
# ======================================================================


# ============================= Functions ==============================
def openfile():  # Function to open select folder window.
    folder_selected = filedialog.askdirectory(title="Select location")
    folder_path.set(folder_selected)


def sort():      # Function to sort files.
    folder = folder_path.get()
    path = folder
    files = os.listdir(path)
    for file in files:
        filename, extension = os.path.splitext(file)
        extension = extension[1:]

        if os.path.exists(path + '/' + extension):
            shutil.move(path + '/' + file, path + '/' + extension + '/' + file)
        else:
            os.mkdir(path + '/' + extension)
            shutil.move(path + '/' + file, path + '/' + extension + '/' + file)
# ======================================================================

folder_path = StringVar()  # Defining folder_path as string.

# ========================== Styling Buttons ===========================
style = ttk.Style()
style.configure('font.TButton', font=(None, 10))
# ======================================================================


# =============================== Labels ===============================
label1 = Label(window, text="Enter Folder Path", font=5)           # Enter folder path text.
label1.grid(row=0, column=0)
entry_label = ttk.Entry(window, textvariable=folder_path, font=5)  # Folder path entry box.
entry_label.grid(row=0, column=1, padx=3)
# ======================================================================


# ============================== Buttons ===============================
open_button = ttk.Button(text="Select", style="font.TButton", command=openfile)  # Select button.
open_button.grid(row=0, column=3)
sort_button = ttk.Button(text="Sort", style="font.TButton", command=sort)        # Sort button.
sort_button.grid(row=1, column=3)
# ======================================================================

window.resizable(False,False)  # Prohibiting resizability.
window.mainloop()              # Run window.

# ========================= End of the program ==========================
