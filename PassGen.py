import cryptography
import tkinter as tk
from tkinter import filedialog as fd
import os


class Window:

    def __init__(self):
        root.title("PassGen")
        if os.name == "posix":
            root.wm_iconbitmap("@"+"pg.xbm")
        elif os.name == "nt":
            root.wm_iconbitmap("pg.ico")
        self.menu()
        self.left()
        self.right()

    def open(self):
        file = fd.askopenfilename()

    def save(self):
        file = fd.asksaveasfilename()

    def menu(self):
        menu = tk.Menu()
        root.config(menu=menu)
        menu1 = tk.Menu(menu, bg="black", fg="white")
        menu.add_cascade(label="File", menu=menu1)
        menu1.add_command(label="Open...", command=self.open)
        menu1.add_command(label="Save...", command=self.save)
        menu1.add_command(label="Exit", command=root.quit)
        menu2 = tk.Menu()
        menu2 = tk.Menu(menu2, bg="black", fg="white")
        menu.add_cascade(label="About", menu=menu2)
        menu2.add_command(label="Help")
        menu2.add_command(label="About")

    def left(self):
        left = tk.LabelFrame(root, text="Left", padx=5,pady=5, bg="black", fg="white")
        left.pack(side="left", expand=True, fill="both")

        encrypt = tk.LabelFrame(left, text="Encrypt", padx=5,pady=5, bg="white", fg="black")
        encrypt.pack(side="top", expand=True, fill="both")

        label1 = tk.Label(encrypt, text="How many passwords generate?", bg="white", fg="black")
        label1.grid(row=0, column=0)
        mb1 = tk.Menubutton(encrypt, text="Select.")
        mb1.grid(row=0, column=1)
        mb1.menu = tk.Menu(mb1)
        mb1["menu"] = mb1.menu
        p_num = tk.IntVar()
        p_num.set(1)
        for i in range(1, 11):
            mb1.menu.add_radiobutton(label=i, variable=p_num, value=i)
        label2 = tk.Label(encrypt, text="Password:", bg="white", fg="black")
        label2.grid(row=1, column=0)

        decrypt = tk.LabelFrame(left, text="Decrypt", padx=5,pady=5, bg="white", fg="black")
        decrypt.pack(side="bottom", expand=True, fill="both")

        b1 = tk.Button(decrypt, text="print",  command=lambda: print(p_num.get()))
        b1.pack()

    def right(self):
        right = tk.LabelFrame(root, text="Right", padx=5, pady=5, bg="black", fg="white")
        right.pack(side="right",expand=True, fill="both")
        t_box = tk.Text(right, padx=5, pady=5, bg="white", fg="black")
        t_box.pack(expand=True, fill="both")


root = tk.Tk()
window = Window()
root.mainloop()
