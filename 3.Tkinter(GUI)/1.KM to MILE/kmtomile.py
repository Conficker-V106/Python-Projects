import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

# window
window = ttk.Window(themename='cyborg')
window.title("Converter")
window.geometry("300x150")
window.minsize(width=400,height=150)

# fuctions

def convert():
    mile = entryInt.get()
    km = mile*1.61
    output_var.set(km)

# title

title_label = ttk.Label(master=window, text = "Miles to Kilometers", font = "calibri 24 bold")
title_label.pack()

# input field 
input_frame = ttk.Frame(master = window)
entryInt = tk.IntVar()
entry = ttk.Entry(master=input_frame,textvariable=entryInt)
button = ttk.Button(master=input_frame,text = 'convert', command=convert)
entry.pack(side="left",padx=10)
button.pack(side="left",padx=10)
input_frame.pack(pady=10)

# output
output_var = tk.StringVar()
output_label = ttk.Label(master=window, textvariable=output_var, font = "calibri 24 bold")
output_label.pack(pady=10)


window.mainloop()