# Combined script which will be compiled into a .exe file for running ElysION log analysis scripts

# Imports

from ctypes import resize
import pathlib
import subprocess
import time
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from ttkthemes import ThemedStyle
import interpreter
import lexer
import parser

# Constants

INSTALL_PATH = "C:\\Users\\tchapman\\source\\repos\\brainrot\\build\\ElysION_LogScripts"
NANOPORE_BLUE = "#0084A9"
NANOPORE_LIGHT_BLUE = "#90C6E7"
NANOPORE_DARK_BLUE = "#0C5A71"
NANOPORE_DARK_GREY_BLUE = "#455560"
NANOPORE_STORM_BLUE = "#49606E"
NANOPORE_DARK_GREY = "#3B3A3A"
NANOPORE_MEDIUM_GREY = "#68767E"
NANOPORE_WARM_GREY = "#BBB2A8"
NANOPORE_LIGHT_GREY = "#F0EFED"
NANOPORE_LIGHT_GREY_1 = "#F9F9FB"
NANOPORE_WHITE = "#FFFFFF"


# Variables

dark_mode = False
selected_filepath = ""

# Functions

def run_script():
    """
    Runs the selected script. If no script has been selected, prints 'No file selected'.
    """
    global selected_filepath
    if selected_filepath:
        subprocess.run(["py", "C:\\Users\\tchapman\\source\\repos\\brainrot\\esolang_files\\interpreter.py",selected_filepath])
    else:
        print("No file selected!")

def browse_files():
    """
    Opens file browser to select which script to run. Looks initially for '.slang' files, can also look for all files (though interpreter will only work with '.slang' files at the moment)
    
    Returns: 
        selected_filepath (str): The path to the selected file
    """
    global selected_filepath
    global label_file_explorer
    script_path = INSTALL_PATH + "\\scripts"
    selected_filepath = filedialog.askopenfilename(initialdir = INSTALL_PATH,
                                          title = "Select a File",
                                          filetypes = (("Slang files",
                                                        "*.slang*"),
                                                       ("all files",
                                                        "*.*")))
      
    if selected_filepath:
        path = pathlib.Path(selected_filepath)
        script_name = str(path.name).replace("_"," ")
        label_file_explorer.configure(text=f"File Opened: {script_name}")
    else:
        label_file_explorer.configure(text="No file selected.")
    return selected_filepath

def help():
    return

def toggle():
    """
    Creates and manages the switch to toggle between dark- and light-mode.
    """
    global dark_mode
    if dark_mode == True:
        root.config(background=NANOPORE_LIGHT_GREY)
        dark_mode_button.config(image=LIGHTMODE,bg=NANOPORE_LIGHT_GREY)
        button_exit.config(bg=NANOPORE_LIGHT_GREY_1,fg=NANOPORE_DARK_BLUE)
        button_explore.config(bg=NANOPORE_LIGHT_GREY_1,fg=NANOPORE_DARK_BLUE)
        style.configure('TButton', background=NANOPORE_MEDIUM_GREY, foreground=NANOPORE_DARK_BLUE, font=('Helvetica', 10, 'bold'))
        style.configure('TLabel', background=NANOPORE_LIGHT_GREY, font=('Helvetica', 10))
        label_file_explorer = Label(root,
                            text="ElysION Log File Script Manager",
                            width=100, height=4,
                            fg=NANOPORE_BLUE,
                            bg=NANOPORE_LIGHT_GREY,
                            font=("Helvetica", 14, "bold"))
        label_file_explorer.grid(column=1,row=1,columnspan=1,padx=10,pady=20)
        ttk.Button(root, text="Run Script", command=run_script).grid(column=1, row=4,padx=10,pady=10)
        dark_mode = False
    else:
        root.config(background=NANOPORE_DARK_GREY_BLUE)
        dark_mode_button.config(image=DARKMODE,bg=NANOPORE_DARK_GREY_BLUE)
        button_exit.config(bg=NANOPORE_LIGHT_GREY,fg=NANOPORE_DARK_BLUE)
        button_explore.config(bg=NANOPORE_LIGHT_GREY,fg=NANOPORE_DARK_BLUE)
        style.configure('TButton', background=NANOPORE_LIGHT_GREY, foreground=NANOPORE_DARK_BLUE, font=('Helvetica', 10, 'bold'))
        style.configure('TLabel', background=NANOPORE_DARK_GREY_BLUE, font=('Helvetica', 10))
        label_file_explorer = Label(root,
                    text="ElysION Log File Script Manager",
                    width=100, height=4,
                    fg=NANOPORE_LIGHT_GREY,
                    bg=NANOPORE_DARK_GREY_BLUE,
                    font=("Helvetica", 14, "bold"))
        label_file_explorer.grid(column=1,row=1,columnspan=1,padx=10,pady=20)
        ttk.Button(root, text="Run Script", command=run_script).grid(column=1, row=4,padx=10,pady=10)
        dark_mode = True


# Tkinter

# Creates the main tkinter window
root = Tk()
root.title("ElysION log file script manager")

# Nanopore logos
LIGHTMODE = PhotoImage(file="C:\\Users\\tchapman\\source\\repos\\brainrot\\ButtonImages\\LightMode.png")
DARKMODE = PhotoImage(file="C:\\Users\\tchapman\\source\\repos\\brainrot\\ButtonImages\\DarkMode.png")

# Sets size of window
root.geometry("600x280")

# Sets background of window to nanopore light grey (hex code at top of method)
root.config(background=NANOPORE_LIGHT_GREY)

# Controls style of buttons and labels in the window
style = ttk.Style()
style.configure('TButton', background=NANOPORE_LIGHT_GREY, foreground=NANOPORE_DARK_BLUE, font=('Helvetica', 10, 'bold'))
style.configure('TLabel', background=NANOPORE_LIGHT_GREY, font=('Helvetica', 10))
label_file_explorer = Label(root,
                    text="ElysION Log File Script Manager",
                    width=100, height=4,
                    fg=NANOPORE_BLUE,
                    bg=NANOPORE_LIGHT_GREY,
                    font=("Helvetica", 14, "bold"))

# Creates the buttons and labels in the window
button_explore = Button(root,
                        text="Browse Files",
                        command=browse_files,
                        bg=NANOPORE_LIGHT_GREY,
                        fg=NANOPORE_DARK_BLUE,
                        font=('Helvetica', 10, 'bold'))

button_exit = Button(root,
                        text="Exit",
                        command=exit,
                        bg=NANOPORE_LIGHT_GREY,
                        fg=NANOPORE_DARK_BLUE,
                        font=('Helvetica', 10, 'bold'))

# Places the buttons and labels in the grid
label_file_explorer.grid(column=1,row=1,columnspan=1,padx=10,pady=20)

button_explore.grid(column=1,row=2,padx=10,pady=10)

button_exit.grid(column=1,row=3,padx=10,pady=10)


root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

# Initialises the button
dark_mode_button = Button(root, image=LIGHTMODE, bd=0, command=toggle,bg=NANOPORE_LIGHT_GREY)

# Places the button
dark_mode_button.grid(column=3,row=1)

# Calls the script when the button is clicked
ttk.Button(root, text="Run Script", command=run_script).grid(column=1, row=4,padx=10,pady=10)

# Main

if __name__ == "__main__":
    root.mainloop()