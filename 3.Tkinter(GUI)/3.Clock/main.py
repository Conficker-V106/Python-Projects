import tkinter as tk
from tkinter import ttk
from time import strftime

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

# Create the main application window
root = tk.Tk()
root.title("Digital Clock")

# Set up the ttkbootstrap style
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 48), padding=20)

# Create the main frame
main_frame = ttk.Frame(root, padding=20)
main_frame.grid(row=0, column=0, sticky="nsew")

# Create the clock label
label = ttk.Label(main_frame)
label.grid(row=0, column=0)

# Call the time function to update the clock
time()

# Start the main event loop
root.mainloop()
