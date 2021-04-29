from tkinter import *
from tkinter import filedialog

file_path = ""

selected_lang = "Python"

lighter_gray = "#3C3F41"
darker_gray = "#2B2B2B"
menu_text_white = "#BBBBBB"
editor_text_white = "#A2AFBD"

param_screen_shown = False


mw = Tk()  # Initialize main window
mw.title("Unsaved - SyntaxBlocks alpha")

def set_window_title():
    mw.title(file_path + " - SyntaxBlocks alpha")


def open_about_screen():
    about_screen = Toplevel(mw, bg=lighter_gray)
    about_screen.title("About SyntaxBlocks")

    about_label = Label(about_screen,
                        text="SyntaxBlocks is an experimental project to help programming learners quickly adapt to "
                             "new programming languages.\n2021 Redline Software.", fg=menu_text_white, bg=lighter_gray)
    close_bttn = Button(about_screen, text="Close",
                        command=about_screen.destroy)
    about_label.pack()
    close_bttn.pack()


def open_help_screen():
    help_screen = Toplevel(mw)
    help_screen.title("Help")

    about_label = Label(help_screen,
                        text="Inserting blocks: click on categories in menubar, click tearoff line at top of category "
                             "to make separate window\n\nBlock types:\n() - function/method\n. - dot notation\n.() - "
                             "dot notation function/method\n+ - operator", fg=menu_text_white, bg=lighter_gray)
    close_bttn = Button(help_screen, text="Close", command=help_screen.destroy)
    about_label.pack()
    close_bttn.pack()


def insert_block_with_params(block: str, b_unit: str):
    block_string = languages[selected_lang][b_unit][block][0]
    params = languages[selected_lang][b_unit][block][1]
    for param in params:
        block_string = block_string.replace(param, param_variables[param].get())
    code_editor.insert(INSERT, block_string)


def show_params_screen(block_key: str, block_unit: str):
    def insert_button_func():
        global param_screen_shown
        insert_block_with_params(block_key, block_unit)
        param_screen_window.destroy()
        param_screen_shown = False

    """
    If there are parameters, allows the user to enter them through a GUI
    :param block_key:
    :param params:
    """
    global code_editor, param_variables, param_labels, param_entries
    global param_screen_shown
    params = languages[selected_lang][block_unit][block_key][1]
    if not param_screen_shown:
        if len(params) > 0:
            # If there are params, only then show the screen, else insert the
            # block instantly
            param_screen_shown = True
            param_screen_window = Toplevel(mw, bg=lighter_gray)
            param_screen_window.title("Insert block: " + block_key)
            global param_variables
            param_variables = dict()
            param_labels = dict()
            param_entries = dict()
            for param in params:
                param_variables[param] = StringVar()
                param_labels[param] = Label(param_screen_window, text=param.replace("_", " ") + ":", bg=lighter_gray,
                                            fg=menu_text_white)
                param_entries[param] = Entry(param_screen_window, bg=darker_gray, fg=editor_text_white,
                                             textvariable=param_variables[param])
                param_labels[param].pack()
                param_entries[param].pack()

            insert_button = Button(param_screen_window, text="Insert", bg="green", fg="white",
                                   command=insert_button_func)
            insert_button.pack()
        else:
            code_editor.insert(INSERT, languages[selected_lang][block_unit][block_key][0])


# Language blocks database
languages = {
    "Python": {
        "Basics": {
            "Text": ["\"\"", []],
            "Add": ["+", []],
            "Subtract": ["-", []],
            "Multiply": ["*", []],
            "Divide": ["/", []],
            "Int divide": ["//", []],
            "Power": ["**", []],
            "Newline character": ["\\n", []],
            "Tab character": ["\\t", []]
        },
        "Blocks": {
            "If": ["if Condition:\n\t", ["Condition"]],
            "If else": ["if :\n\t\nelse:\n\t", ["Condition"]],
            "For loop with simple counter": ["for Iterable in range(Stop):\n\t", ["Iterable", "Stop"]],
            "For loop with advanced counter (start, stop, step)": ["for Iterable in range(Start, Stop, Step)\n\t",
                                                                   ["Iterable", "Start", "Stop", "Step"]],
            "While loop": ["while Condition:\n\t", ["Condition"]]
        },
        "Functions": {
            "Print to console ()": ["print(Message)", ["Message"]],
            "Evaluate string expression and return result ()": ["eval(Expression)", ["Expression"]],
            "Execute string statement ()": ["exec(Statement)", ["Statement"]],
            "Length of an object ()": ["len(Object)", ["Object"]],
            "Read line from file": ["File.readline()", ["File"]]
        }
    },
    "Python for GTK": {
        "Basics": {
            "Main boilerplate": ["import gi\ngi.require_version(\"Gtk\", \"3.0\")\nfrom gi.repository import Gtk\n\nwindow = Gtk.Window(title=Window_title)\nwindow.show()\nwindow.connect(\"destroy\", Gtk.main_quit)\nGtk.main()", ["Window_title"]]
        }
    },
    "C#": {
        "Basics": {
            "Main boilerplate": ["using System;\n\nclass Class_name\n{\n\npublic static void Main(string[] args)\n{"
                                 "\n\t\n}\n}", ["Class_name"]],
            "Integer data type": ["int", []],
            "64-bit signed integer": ["long", []],
            "Floating point data type": ["float", []],
            "Double precision float data type": ["double", []],
            "Byte data type": ["byte", []],
            "Character data type": ["char", []],
            "String data type": ["string", []],
            "Boolean data type": ["bool", []],
            "New void function": ["void Function_name(){\n\n}", ["Function_name"]],
            "New custom function": ["Return_type Function_name(Arguments_(optional))\n{\n\t\n}",
                                    ["Return_type", "Function_name", "Arguments_(optional)"]],
            "Public modifier": ["public", []],
            "Protected modifier": ["protected", []],
            "Private modifier": ["private", []],
            "Use external module": ["using Module;", ["Module"]]
        },
        "Operators": {
            "Assign": ["=", []],
            "Add": ["+", []]
        },
        "Functions": {
            "Write line to console ()": ["Console.WriteLine(Message);", ["Message"]],
            "Convert string to integer ()": ["AsInt(String)", ["String"]],
            "Check if value is integer ()": ["IsInt(Value)", ["Value"]],
            "Convert value to float ()": ["AsFloat(Value)", ["Value"]],
            "Check if value is float ()": ["IsFloat(Value)", ["Value"]],
            "Convert string into date/time ()": ["AsDateTime(String)", ["String"]]
        },
        "Blocks": {
            "If": ["if(Condition)\n{\n\t\n}", ["Condition"]],
            "If else": ["if(Condition)\n{\n\t\n}\nelse\n{\t\n}", ["Condition"]],
            "For loop (simple)": ["for(int Iterable = Start; Iterable < Stop; Iterable++)\n{\n\t\n}",
                                  ["Iterable", "Start", "Stop"]],
            "For loop (advanced)": ["for(int Iterable = Start; Condition; Increment)\n{\n\t\n}",
                                    ["Iterable", "Start", "Condition", "Increment"]],
        }
    },
    "C# for Unity": {
        "General": {"Unity Event data type": ["UnityEvent", []],
                    "Invoke Unity Event": ["Event.Invoke()", ["Event"]],
                    "MonoBehaviour class": ["public class Class_name : MonoBehaviour{\n\n}", ["Class_name"]],
                    "Add editor field to private variable (add before private declaration)": ["[SerializeField]", []],
                    },
        "Functions": {
            "Call at game start": ["void Start(){\n}", []]
        },
        "GameObject": {
            "Set active .()": [".setActive(True/False)", ["True/False"]]
        },
        "Transform": {
            "Get transform position .": ".Transform.position",
            "Move (translate) Transform .()": [".Translate(Vector)", ["Vector"]],
            "Rotate Transform .()": [".Rotate(Vector)", ["Vector"]],
            "Create new Vector2": ["new Vector2(X, Y)", ["X", "Y"]],
            "Create new Vector3": ["new Vector3(X, Y, Z)", ["X", "Y", "Z"]]
        },
        "UI": {
            "Text data type": ["Text", []],
            "String to be included in text module <Text>.": [".text", []]
        }
    },
    "HTML": {
        "Basics": {
            "Main boilerplate": ["<!DOCTYPE html>\n<html>\n<head>\n\t<title>Website_title</title>\n</head>\n<body>\n\n"
                                 "</body>\n</html>", ["Website_title"]],
            "Heading Level 1": ["<h1></h1>", []],
            "Heading Level 2": ["<h2></h2>", []],
            "Heading Level 3": ["<h3></h3>", []],
            "Heading Level 4": ["<h4></h4>", []],
            "Heading Level 5": ["<h5></h5>", []],
            "Heading Level 6": ["<h6></h6>", []],
            "Paragraph": ["<p></p>", []],
            "Div container": ["<div class=\"Class_name\" id=\"Identifier\"></div>", ["Class_name", "Identifier"]],
            "Span": ["<span class=\"Class_name\" id=\"Identifier\">", ["Class_name", "Identifier"]]
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

    set_window_title()
    
    file_in.close()


def save_file():
    file_out = open(file_path, "w")

    for line in code_editor.get("1.0", "end-1c"):
        print(line, file=file_out, end="")

    file_out.close()


def save_as():
    global file_path
    file_out = filedialog.asksaveasfile()

    for line in code_editor.get("1.0", "end-1c"):
        print(line, file=file_out, end="")

    file_out.close()


# Configure menus

file_menu = Menu(mw, bg="#3C3F41", fg="#BBBBBB", activebackground="#2E7AD0")
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save as", command=save_as)
file_menu.add_separator()
file_menu.add_command(label="About", command=open_about_screen)
file_menu.add_command(label="Help", command=open_help_screen)

lang_menu = Menu(mw, bg="#3C3F41", fg="#BBBBBB", activebackground="#2E7AD0")
for lang in languages.keys():
    exec("lang_menu.add_command(label=lang, command=lambda: change_lang(\"" + lang + "\"))")

menubar = Menu(mw, bg="#3C3F41", fg="#BBBBBB", activebackground="#2E7AD0")
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
        exec("{0}_menu = Menu(mw, bg=\"#3C3F41\", fg=\"#BBBBBB\", activebackground=\"#2E7AD0\")".format(
            unit.replace(" ", "")))  # Create a block group
        for block in languages[selected_lang][unit].keys():
            exec(
                unit +
                "_menu.add_command(label=block, command=lambda: show_params_screen(\"" + block + "\", \"" + unit + "\"))")  # Add a block to a category

        exec("menubar.add_cascade(label=\"{0}\", menu={1}_menu)".format(
            unit, unit.replace(" ", "")))  # Add current block group to menu


change_lang("Python")  # Set the default language to Python

# Here we create the block groups visible in the menu bar


# Create the code editor module
code_editor = Text(mw, bg="#2B2B2B", fg="#A2AFBD", insertbackground="white", highlightthickness=0, insertwidth=3)

# Pack the code editor module into the container window
code_editor.pack(fill="both", expand=True)

mainloop()  # TkInter main loop
