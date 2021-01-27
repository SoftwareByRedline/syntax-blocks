from tkinter import *
from tkinter import filedialog

file_path = ""

mw = Tk()  # Initialize main window
mw.title("SyntaxBlocks alpha")


def open_file():
    global file_path
    file_path = filedialog.askopenfilename()
    file_in = open(file_path, "r")
    code_editor.delete("1.0", "end-1c")
    for line in file_in:
        code_editor.insert("end-1c", line)

    file_in.close()

def save_file():
    file_out = open(file_path, "w")

    for line in code_editor.get("1.0", "end-1c"):
        print(line, file=file_out, end="")

    file_out.close()

# Configure menus
file_menu = Menu(mw)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)

menubar = Menu(mw)
mw.config(menu=menubar)
menubar.add_cascade(label="File", menu=file_menu)


code_editor = Text(mw)

code_editor.pack()

mainloop()  # TkInter main loop
