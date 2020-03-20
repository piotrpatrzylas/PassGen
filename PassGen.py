import cryptography
import tkinter as tk
from tkinter import filedialog as fd
import os


class Window:

    def __init__(self, root):
        self.top = root
        root.title("PassGen")
        if os.name == "posix":
            root.wm_iconbitmap("@"+"pg.xbm")
        elif os.name == "nt":
            root.wm_iconbitmap("pg.ico")
        self.menu()

    def open(self):
        file = fd.askopenfilename()

    def save(self):
        file = fd.asksaveasfilename()

    def menu(self):
        menu = tk.Menu()
        root.config(menu=menu)
        menu1 = tk.Menu(menu)
        menu.add_cascade(label="File", menu=menu1)
        menu1.add_command(label="Open...", command=self.open)
        menu1.add_command(label="Save...", command=self.save)
        menu1.add_command(label="Exit", command=root.quit)
        menu2 = tk.Menu()
        menu2 = tk.Menu(menu2)
        menu.add_cascade(label="About", menu=menu2)


root = tk.Tk()
window = Window(root)
root.mainloop()