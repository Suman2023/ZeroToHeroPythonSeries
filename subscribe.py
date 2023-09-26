import tkinter as tk
from tkinter import font
import webbrowser as wb
import time

def subscribe():
    wb.open("https://www.youtube.com/channel/UCGxmYrECkEGtNvTwkJeANKQ?sub_confirmation=1")

def update_time():
    now = time.strftime("%H:%M:%S")
    current_time.config(text=now)
    root.after(1000, update_time) # calls tjhis function every 1000ms i.e. 1s

# Create the main application window
root = tk.Tk()
root.title("Tkinter Example")

# Custome Font
custom_font = font.Font(size=24)

# Set the window size (width x height)
window_width = 800
window_height = 600
root.geometry(f"{window_width}x{window_height}")

# Create a label widget
current_time = tk.Label(root, text=f"", font=custom_font)
current_time.pack()

# Create a button widget
button = tk.Button(root, text="Subscribe",font=custom_font, bg="red", width=25, height=1, command=subscribe)
button.pack(pady=250)

# Create a label widget
copyright = tk.Label(root, text="© Lets Code Together")
copyright.pack()

# Start the loop for updating text
update_time()

# Start the Tkinter event loop
root.mainloop()
