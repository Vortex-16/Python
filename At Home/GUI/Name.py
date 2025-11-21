import tkinter as tk

def show_name():
    name = entry.get()
    output_label.config(text="Your Name: " + name)

# GUI Window
window = tk.Tk()
window.title("Name Printer")

# Input label
tk.Label(window, text="Enter your name:", font=("Arial", 14)).pack(pady=10)

# Input box
entry = tk.Entry(window, font=("Arial", 14), width=25)
entry.pack()

# Button
tk.Button(window, text="Print Name", font=("Arial", 14),
          command=show_name).pack(pady=20)

# Output label
output_label = tk.Label(window, text="", font=("Arial", 16), fg="green")
output_label.pack()

window.mainloop()
