from tkinter import *
from tkinter import filedialog

file_path = ""

selected_lang = "Python"

mw = Tk()  # Initialize main window
mw.title("SyntaxBlocks alpha")


def open_about_screen():
    about_screen = Toplevel(mw)
    about_screen.title("About SyntaxBlocks")

    about_label = Label(about_screen,
                        text="SyntaxBlocks is an experimental project to help programming learners quickly adapt to "
                             "new programming languages.\n2021 Redline Software.")
    close_bttn = Button(about_screen, text="Close", command=about_screen.destroy)
    about_label.pack()
    close_bttn.pack()


def open_help_screen():
    help_screen = Toplevel(mw)
    help_screen.title("Help")

    about_label = Label(help_screen,
                        text="Inserting blocks: click on categories in menubar, click tearoff line at top of category "
                             "to make separate window\n\nBlock types:\n() - function/method\n. - dot notation\n.() - "
                             "dot notation function/method\n+ - operator")
    close_bttn = Button(help_screen, text="Close", command=help_screen.destroy)
    about_label.pack()
    close_bttn.pack()


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
            "Power": "^",
            "Newline character": "\\n",
            "Tab character": "\\t"
        },
        "Blocks": {
            "If": "if :\n\t",
            "If else": "if :\n\t\nelse:\n\t",
            "For loop with simple counter": "for  in range():\n\t",
            "For loop with advanced counter (start, stop, step)": "for  in range( , , )\n\t",
            "While loop": "while :\n\t"
        },
        "Functions": {
            "Print to console ()": "print()",
            "Evaluate string statement and return result ()": "eval()",
            "Execute string statement ()": "exec()",
            "Length of an object ()": "len()",
            "Read line from file .()": ".readline()"
        }
    },
    "C#": {
        "Basics": {
            "Integer data type": "int",
            "64-bit signed integer": "long",
            "Floating point data type": "float",
            "Double precision float data type": "double",
            "Byte data type": "byte",
            "Character data type": "char",
            "String data type": "String",
            "Boolean data type": "bool",
            "Void function": "void  (){\n\n}",
            "Public modifier": "public",
            "Protected modifier": "protected",
            "Private modifier": "private",
            "Use external module": "using ;"
        },
        "Operators": {
            "Assign": "=",
            "Add": "+"
        },
        "Functions": {
            "Write line to console ()": "Console.WriteLine();",
            "Convert string to integer ()": "AsInt()",
            "Check if value is integer ()": "IsInt()",
            "Convert value to float ()": "AsFloat()",
            "Check if value is float ()": "IsFloat()",
            "Convert string into date/time ()": "AsDateTime()"
        },
        "Blocks": {},
    },
    "C# for Unity": {
        "General": {"Unity Event data type": "UnityEvent",
            "Invoke Unity Event .()": ".Invoke()",
            "MonoBehaviour class": "public class  : MonoBehaviour{\n\n}"},
        "Transform":{
            "Move (translate) Transform .(vector)": ".Translate()",
            "Rotate Transform .(vector)": ".Rotate()",
            "Create new Vector2 (x, y)": "new Vector2()",
            "Create new Vector3 (x, y, z)": "new Vector3()"
        }
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
file_menu.add_separator()
file_menu.add_command(label="About", command=open_about_screen)
file_menu.add_command(label="Help", command=open_help_screen)

lang_menu = Menu(mw)
for lang in languages.keys():
    exec("lang_menu.add_command(label=lang, command=lambda: change_lang(\"" + lang + "\"))")

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

code_editor.pack(fill="both", expand=True)  # Pack the code editor module into the container window

mainloop()  # TkInter main loop
