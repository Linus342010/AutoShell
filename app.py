import customtkinter as ctk
from tkinter import filedialog
import subprocess
import webbrowser

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("Autoshell (AShell)")
app.geometry("800x400")
app.iconbitmap("autoshell.ico")


def create_script():
    path = filedialog.asksaveasfile(title="Create Script",defaultextension=".ashell",filetypes=[("Autoshell Script", "*.ashell")])
    if path:
        with open(path.name, "a"):
            pass
        subprocess.run(["notepad.exe", path.name])

def open_script():
    path = filedialog.askopenfile(title="Open Script",filetypes=[("Autoshell Script", "*.ashell")])
    if path:
        subprocess.run(["notepad.exe", path.name])

def open_github():
    webbrowser.open("https://github.com/Linus342010/AutoShell")



app.grid_columnconfigure(0, weight=0)
app.grid_columnconfigure(1, weight=1)
app.grid_rowconfigure(0, weight=1)


left_frame = ctk.CTkFrame(app, width=200)
left_frame.grid(row=0, column=0, sticky="ns", padx=(15, 5), pady=15)

create_button = ctk.CTkButton(left_frame,text="Create Script",command=create_script)
create_button.pack(fill="x", padx=10, pady=5)

open_button = ctk.CTkButton(left_frame,text="Open Script",command=open_script)
open_button.pack(fill="x", padx=10, pady=5)


right_frame = ctk.CTkFrame(app)
right_frame.grid(row=0, column=1, sticky="nsew", padx=(5, 15), pady=15)
right_frame.grid_columnconfigure(0, weight=1)

title = ctk.CTkLabel(right_frame, text="Welcome to Autoshell", font=ctk.CTkFont(size=20, weight="bold"))
title.pack(pady=10)

info = ctk.CTkLabel(right_frame, text="Autoshell is a powerful scripting tool that allows you to automate tasks.", wraplength=800, justify="left")
info.pack(pady=10)

github_link = ctk.CTkButton(right_frame, text="Visit GitHub Repository", command=open_github)
github_link.pack(pady=10)


app.mainloop()