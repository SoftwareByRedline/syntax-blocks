from tkinter import *
from tkinter import filedialog

file_path = ""

selected_lang = "Python"

mw = Tk()  # Initialize main window
mw.title("SyntaxBlocks alpha")

# Language blocks database
languages = {
    "Python": {
        "Basics": {
            "Text": "\"\"",
            "Add": "+",
            "Subtract": "-",
            "Multiply": "*",
            "Divide": "/",
            "Int divide": "//",
            "Power": "^"
        },
        "Blocks": {
            "If": "if :\n",
            "If else": "if :\n\nelse:\n",
            "For loop with simple counter": "for  in range()",
            "For loop with advanced counter (start, stop, step)": "for  in range( , , )",
            "While loop": "while :\n"
        },
        "Functions": {
            "Print to console": "print()",
            "Evaluate string statement and return result": "eval()",
            "Execute string statement": "exec()",
            "Length of an object": "len()",
        }
    },
    "C#": {
        "Basics": {},
        "Blocks": {},
        "Unity": {}
    }
}  # List of programming languages available in the app


def open_file():  # Open file method
    global file_path  # Save the open file path in a global variable
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


def save_as():
    global file_path
    file_path = filedialog.asksaveasfile()
    print(type(file_path))

    file_out = open(file_path, "w")

    for line in code_editor.get("1.0", "end-1c"):
        print(line, file=file_out, end="")

    file_out.close()


# Configure menus

file_menu = Menu(mw)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save as", command=save_as)

lang_menu = Menu(mw)
for lang in languages.keys():
    lang_menu.add_command(label=lang, command=lambda: exec("change_lang(\"%s\")" % lang))

menubar = Menu(mw)
mw.config(menu=menubar)
menubar.add_cascade(label="File", menu=file_menu)
menubar.add_cascade(label="Language", menu=lang_menu)
menubar.add_separator()


def change_lang(input_lang: str):
    global selected_lang

    """
    Function to change language
    """
    try:
        for entry in languages[selected_lang].keys():
            menubar.delete(entry)
    except:
        pass
    selected_lang = input_lang
    for unit in languages[selected_lang].keys():
        exec(unit + "_menu = Menu(mw)")  # Create a block group
        for block in languages[selected_lang][unit].keys():
            exec(
                unit + "_menu.add_command(label=block, command=lambda: code_editor.insert(INSERT, languages["
                       "selected_lang][\"" + unit + "\"][\"" + block + "\"]))")  # Add a block to a category

        exec("menubar.add_cascade(label=\"{0}\", menu={1}_menu)".format(unit, unit))  # Add current block group to menu


change_lang("Python")  # Set the default language to Python

# Here we create the block groups visible in the menu bar


code_editor = Text(mw)  # Create the code editor module

code_editor.pack()  # Pack the code editor module into the container window

mainloop()  # TkInter main loop
