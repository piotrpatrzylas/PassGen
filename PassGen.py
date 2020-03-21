from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import filedialog as fd
import os
import secrets
from random import randint
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def encrypt_algorithm(word):
    b_password = word.encode()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=b'\xb4\xeb\xc4B\x10l;\xe0\xb6\xc7\x9eD\xe3x\xc9\xc2',
        iterations=150000,
        backend=default_backend())
    key = base64.urlsafe_b64encode(kdf.derive(b_password))
    f = Fernet(key)
    return f


class Window:

    def __init__(self, root):
        self.database = []
        self.root = root
        self.root.title("PassGen")
        self.text = bytes()
        if os.name == "posix":
            self.root.wm_iconbitmap("@"+"pg.xbm")
        elif os.name == "nt":
            self.root.wm_iconbitmap("pg.ico")

        self.menu()

        left = tk.LabelFrame(self.root, padx=20, pady=20)
        left.pack(side="left", expand=True, fill="both")

        encrypt = tk.LabelFrame(left, text="Encrypt", padx=20, pady=20, relief="raised")
        encrypt.pack(side="top", expand=True, fill="x")

        label1 = tk.Label(encrypt, text="How many passwords generate?")
        label1.grid(row=0, column=0)
        self.p_num = tk.IntVar()
        self.p_num.set(1)
        mb1 = tk.Menubutton(encrypt, text=self.p_num.get())
        mb1.grid(row=0, column=1)
        mb1.menu = tk.Menu(mb1)
        mb1["menu"] = mb1.menu
        for i in range(1, 11):
            mb1.menu.add_radiobutton(label=i, variable=self.p_num, value=i,
                                     command=lambda: mb1.configure(text=self.p_num.get()))

        label2 = tk.Label(encrypt, text="Password:")
        label2.grid(row=2, column=0)
        self.entry1 = tk.Entry(encrypt)
        self.entry1.grid(row=2, column=1)

        button1 = tk.Button(encrypt, text="Encrypt", command=self.encrypt_fun)
        button1.grid(row=3, column=0, columnspan=2)

        decrypt = tk.LabelFrame(left, text="Decrypt", padx=20, pady=20, relief="raised")
        decrypt.pack(side="bottom", expand=True, fill="x")

        label3 = tk.Label(decrypt, text="Password:")
        label3.grid(row=0, column=0)
        self.entry2 = tk.Entry(decrypt)
        self.entry2.grid(row=0, column=1)

        button2 = tk.Button(decrypt, text="Decrypt", command=self.decrypt_fun)
        button2.grid(row=1, column=0, columnspan=2)

        right = tk.LabelFrame(self.root, padx=5, pady=5)
        right.pack(side="right",expand=True, fill="both")
        self.t_box = tk.Text(right, padx=5, pady=5, bg="white", fg="black", state="disabled")
        self.t_box.pack(expand=True, fill="both")

    def menu(self):
        menu = tk.Menu()
        self.root.config(menu=menu)
        menu1 = tk.Menu(menu)
        menu.add_cascade(label="File", menu=menu1)
        menu1.add_command(label="Open...", command=self.open)
        menu1.add_command(label="Save...", command=self.save)
        menu1.add_command(label="Exit", command=self.root.quit)
        menu2 = tk.Menu()
        menu2 = tk.Menu(menu2)
        menu.add_cascade(label="About", menu=menu2)
        menu2.add_command(label="Help", command=self.help)
        menu2.add_command(label="About", command=self.about)

    def open(self):
        file = fd.askopenfile(mode="rb", defaultextension=".pgen",
                              filetypes=(("pgen files", "*.pgen"), ("all files", "*.*")),
                              title="Select file")
        self.text = file.read()
        self.t_box.configure(state="normal")
        self.t_box.delete(1.0, tk.END)
        self.t_box.insert(tk.INSERT, self.text)
        self.t_box.configure(state="disabled")

    def save(self):
        location = fd.asksaveasfilename(confirmoverwrite=True, defaultextension=".pgen",
                                        filetypes=(("pgen files", "*.pgen"), ("all files", "*.*")),
                                        title="Select file")
        file = open(location, "w")
        v1 = self.database
        for i in self.database:
            file.write(i+"\n")
        file.close()
        with open(location, "rb") as fe:
            data = fe.read()
        key = encrypt_algorithm(self.database[0])
        encrypted_data = key.encrypt(data)
        with open(location, "wb") as fe2:
            fe2.write(encrypted_data)

    def encrypt_fun(self):
        self.database = []
        p_phrase = self.entry1.get()
        self.database.append(p_phrase)
        pass_num = self.p_num.get()
        self.t_box.configure(state="normal")

        self.t_box.delete(1.0, tk.END)
        self.t_box.insert(1.0, "File password: " + p_phrase + "\n")
        self.t_box.insert(tk.END, "Number of passwords generated: " + str(pass_num) + "\n")

        alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        for p in range(pass_num):
            secret_word = ''.join(secrets.choice(alphabet) for el in range(randint(25, 50)))
            self.database.append(secret_word)
            self.t_box.insert(tk.END, secret_word + "\n")
        self.t_box.configure(state="disabled")

    def decrypt_fun(self):
        match1 = self.entry2.get()
        f = encrypt_algorithm(match1)
        decoded = f.decrypt(bytes(self.text)).decode().split()
        match2 = decoded[0]
        if match1 == match2:
            self.t_box.configure(state="normal")
            self.t_box.delete(1.0, tk.END)
            self.t_box.insert(1.0, "File password: " + str(decoded[0])+"\n")
            self.t_box.insert(tk.END, "Number of passwords generated: " + str(len(decoded)-1) + "\n")
            for i in range(1, len(decoded)):
                self.t_box.insert(tk.END, str(decoded[i]) + "\n")
            self.t_box.configure(state="disabled")

    def help(self):
        pass

    def about(self):
        pass


top = tk.Tk()
window = Window(top)
top.mainloop()
