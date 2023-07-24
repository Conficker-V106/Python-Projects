import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttkbst

def calculate_bmi():
    weight = float(weight_var.get() or weight_entry.get())
    height = float(height_var.get() or height_entry.get()) / 100  # Convert height from cm to meters
    bmi = weight / (height ** 2)
    bmi_result_label.config(text=f"BMI: {bmi:.2f}")
    bmi_category = get_bmi_category(bmi)
    bmi_category_label.config(text=f"Category: {bmi_category}")

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 24.9 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

# Create the main application window
root = tk.Tk()
root.title("BMI Calculator")

# Set up the ttkbootstrap style
style = ttkbst.Style(theme="morph")
style.configure("TLabel", padding=10)

# Create the main frame
main_frame = ttk.Frame(root, padding=20)
main_frame.grid(row=0, column=0, sticky="nsew")

# Weight and height variables for Entry fields and Scale widgets
weight_var = tk.DoubleVar()
height_var = tk.DoubleVar()

# Create the widgets
weight_label = ttk.Label(main_frame, text="Weight (kg):")
weight_entry = ttk.Entry(main_frame, textvariable=weight_var)
weight_scale = ttk.Scale(main_frame, variable=weight_var, from_=30, to=150, length=200)
height_label = ttk.Label(main_frame, text="Height (cm):")
height_entry = ttk.Entry(main_frame, textvariable=height_var)
height_scale = ttk.Scale(main_frame, variable=height_var, from_=100, to=250, length=200)
calculate_button = ttk.Button(main_frame, text="Calculate", command=calculate_bmi)
bmi_result_label = ttk.Label(main_frame, text="BMI: ")
bmi_category_label = ttk.Label(main_frame, text="Category: ")

# Place the widgets using grid layout
weight_label.grid(row=0, column=0)
weight_entry.grid(row=0, column=1)
weight_scale.grid(row=1, column=1,pady=5)
height_label.grid(row=2, column=0)
height_entry.grid(row=2, column=1)
height_scale.grid(row=3, column=1,pady=5)
calculate_button.grid(row=4, columnspan=3)
bmi_result_label.grid(row=5, columnspan=3)
bmi_category_label.grid(row=6, columnspan=3)

# Start the main event loop
root.mainloop()
