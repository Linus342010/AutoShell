import customtkinter as ctk
from tkinter import filedialog
import subprocess
import src.log

app = ctk.CTk()
app.title("Autoshell")
app.geometry("800x400")
app.iconbitmap("autoshell.ico")


def create_script():
    path = filedialog.asksaveasfile(title="Create Script",defaultextension=".ashell",filetypes=[("Autoshell Script", "*.ashell")])

    if path:
        with open(path, "a"):
            pass
        subprocess.run(["notepad.exe", path.name])

def open_script():
    path = filedialog.askopenfile(title="Open Script",filetypes=[("Autoshell Script", "*.ashell")])

    if path:
        subprocess.run(["notepad.exe", path.name])


create_script_button = ctk.CTkButton(app, text="Create Script", command=create_script)
create_script_button.pack(pady=20, padx=20, fill="x")

open_script_button = ctk.CTkButton(app, text="Open Script", command=open_script)
open_script_button.pack(pady=10, padx=20, fill="x")

text_label = ctk.CTkLabel(app, text="AutoShell", font=ctk.CTkFont(size=20))
text_label.pack(pady=20, padx=20)
text_label2 = ctk.CTkLabel(app, text="A simple tool to automate tasks on your computer using scripts.", font=ctk.CTkFont(size=14))
text_label2.pack(pady=10, padx=20)

app.mainloop()