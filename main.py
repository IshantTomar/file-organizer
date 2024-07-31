# ======================== Importing Libraries ========================
import os                       # For interacting with the operating system.
import shutil                   # To move files.
import customtkinter            # To make GUI.
from customtkinter import *     # To make GUI.
from tkinter import filedialog  # To open file directories.
# ======================================================================


# =============================== Window ===============================
window = CTk()                   # Creating an instance of Tkinter frame.
window.title("File Organizer")   # Window name.
window.iconbitmap("icon.ico")    # Window icon.
set_appearance_mode("dark")      # Window appearance.
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
            sorted_label.configure(text=" Sorted!")
        else:
            os.mkdir(path + '/' + extension)
            shutil.move(path + '/' + file, path + '/' + extension + '/' + file)
            sorted_label.configure(text=" Sorted!")
# ======================================================================

folder_path = StringVar()  # Defining folder_path as string.

# ======================================================================


# =============================== Labels ===============================
label1 = CTkLabel(window, text="Enter Folder Path: ",  font=("Arial", 15))             # Enter folder path text.
label1.grid(row=0, column=0)
entry_label = CTkEntry(window, textvariable=folder_path,  font=("Arial", 15))          # Folder path entry box.
entry_label.grid(row=0, column=1, padx=3,  sticky="w")
sorted_label = CTkLabel(window, text="",  font=("Arial", 15), text_color="lightblue")  # To show files are sorted.
sorted_label.grid(row=1, column=1, sticky="w")
# ======================================================================


# ============================== Buttons ===============================
open_button = CTkButton(window, text="Select", font=("Arial", 15), width=60, command=openfile)  # Select button.
open_button.grid(row=0, column=3, pady=5)
sort_button = CTkButton(window, text="Sort", font=("Arial", 15), width=60, command=sort)        # Sort button.
sort_button.grid(row=1, column=3)
# ======================================================================

window.resizable(False,False)  # Prohibiting resizability.
window.mainloop()              # Run window.

# ========================= End of the program ==========================
