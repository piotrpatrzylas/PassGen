from cryptography.fernet import Fernet
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
        self.main()


    def open(self):
        file = fd.askopenfilename()

    def save(self):
        file = fd.asksaveasfilename()

    def help(self):
        pass

    def about(self):
        pass

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
        menu2.add_command(label="Help", command=self.help)
        menu2.add_command(label="About", command=self.about)

    def main(self):
        left = tk.LabelFrame(root, padx=20,pady=20)
        left.pack(side="left", expand=True, fill="both")

        encrypt = tk.LabelFrame(left, text="Encrypt", padx=20,pady=20, relief="raised")
        encrypt.pack(side="top", expand=True, fill="x")

        label1 = tk.Label(encrypt, text="How many passwords generate?")
        label1.grid(row=0, column=0)
        p_num = tk.IntVar()
        p_num.set(1)
        mb1 = tk.Menubutton(encrypt, text=p_num.get())
        mb1.grid(row=0, column=1)
        mb1.menu = tk.Menu(mb1)
        mb1["menu"] = mb1.menu
        for i in range(1, 11):
            mb1.menu.add_radiobutton(label=i, variable=p_num, value=i, command=lambda: mb1.configure(text=p_num.get()))

        label2 = tk.Label(encrypt, text="Password:")
        label2.grid(row=2, column=0)
        entry1 = tk.Entry(encrypt)
        entry1.grid(row=2, column=1)

        def encrypt_fun():
            passphrase = entry1.get()
            passnum = p_num.get()
            t_box.configure(state="normal")

            t_box.delete(1.0, tk.END)
            t_box.insert(1.0, "File password: "+passphrase+"\n")
            t_box.insert(tk.END, "Number of passwords generated: "+str(passnum))

            global encyptio

            encyptio = t_box.get(1.0, tk.END)
            print(encyptio)

            t_box.configure(state="disabled")

        button1 = tk.Button(encrypt, text="Encrypt", command=encrypt_fun)
        button1.grid(row=3, column=0, columnspan=2)

        decrypt = tk.LabelFrame(left, text="Decrypt", padx=20,pady=20, relief="raised")
        decrypt.pack(side="bottom", expand=True, fill="x")

        label3 = tk.Label(decrypt, text="Password:")
        label3.grid(row=0, column=0)
        entry2 = tk.Entry(decrypt)
        entry2.grid(row=0, column=1)

        button2 = tk.Button(decrypt, text="Decrypt")
        button2.grid(row=1, column=0, columnspan=2)

        right = tk.LabelFrame(root, padx=5, pady=5)
        right.pack(side="right",expand=True, fill="both")
        t_box = tk.Text(right, padx=5, pady=5, bg="white", fg="black", state="disabled")
        t_box.pack(expand=True, fill="both")


root = tk.Tk()
window = Window()
root.mainloop()
