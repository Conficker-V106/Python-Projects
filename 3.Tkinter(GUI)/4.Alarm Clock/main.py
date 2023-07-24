import tkinter as tk
from tkinter import ttk
from time import strftime
import pygame
import ttkbootstrap as ttkbst

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

def set_alarm():
    alarm_time = alarm_entry.get()
    if alarm_time.strip() != "":
        alarm_button.config(state="disabled")
        alarm_label.config(text=f"Alarm set for {alarm_time}")
        update_alarm_time(alarm_time)

def update_alarm_time(alarm_time):
    current_time = strftime('%H:%M')
    if current_time == alarm_time:
        alarm_button.config(state="normal")
        alarm_label.config(text=f"ALARM!!")
        play_alarm_sound()
    else:
        alarm_label.after(1000, lambda: update_alarm_time(alarm_time))

def play_alarm_sound():
    try:
        pygame.mixer.init()
        pygame.mixer.music.load("/home/xerjamar/Projects/3.Tkinter(GUI)/4.Alarm Clock/ama.wav")
        pygame.mixer.music.play()
    except Exception as e:
        print(f"Error playing the sound: {e}")

# Create the main application window
root = tk.Tk()
root.title("Alarm Clock")

# Set up the ttkbootstrap style
style = ttkbst.Style(theme="minty")  

# Create the main frame
main_frame = ttk.Frame(root, padding=20)
main_frame.grid(row=0, column=0, sticky="nsew")

# Create the clock label
label = ttk.Label(main_frame, font=("Helvetica", 48))
label.grid(row=0, column=0, columnspan=2)

# Create the alarm label and entry
alarm_label = ttk.Label(main_frame, text="Set alarm time (HH:MM):", font=("Helvetica", 16))
alarm_label.grid(row=1, column=0, columnspan=2)
alarm_entry = ttk.Entry(main_frame, font=("Helvetica", 24))
alarm_entry.grid(row=2, column=0, pady=10,padx=5)
alarm_button = ttk.Button(main_frame, text="Set Alarm", command=set_alarm)
alarm_button.grid(row=2, column=1, pady=10)

# Call the time function to update the clock
time()

# Start the main event loop
root.mainloop()
