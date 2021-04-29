import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

file_path = ""
selected_lang = "Python"
param_screen_shown = False

window = Gtk.Window(title="Unsaved - SyntaxBlocks alpha")
window.show()
window.connect("destroy", Gtk.main_quit)


def set_window_title():
    window.set_title(file_path + " - SyntaxBlocks alpha")


def open_about_screen():
    about_screen = Gtk.Window(title="About SyntaxBlocks")
    about_screen.show()
    about_screen.connect("destroy", Gtk.main_quit)


Gtk.main()
