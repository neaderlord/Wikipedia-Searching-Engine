import tkinter
from tkinter import*
import tkinter as tk
import webbrowser
import customtkinter
from tkinter import messagebox

#Tkinter Kurulumu
ekran = tk.Tk()
ekran.title("Wikipedia Makale Bulucu")
ekran.geometry("400x200")

def search():
    sözcük = textb.get("1.0", "end-1c")
    if textb == "":
        messagebox.showerror("Lütfen Bir Girdi Giriniz!")
    webbrowser.open_new("https://www.wikipedia.org/wiki/"+ sözcük)

#Text Box
textb = customtkinter.CTkTextbox(master=ekran, height=20, width=250)
textb.place(x=75, y=50)

#Buton
buton = customtkinter.CTkButton(master=ekran, text="Search",fg_color="Green", command=search)
buton.pack(side=BOTTOM, pady=40)

mainloop()