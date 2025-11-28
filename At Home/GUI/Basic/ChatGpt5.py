import tkinter as tk

root = tk.Tk()
root.geometry("400x300")

entry = tk.Entry(root, font=("Arial", 14))
entry.pack()

def show_name():
    name = entry.get()
    print("Hello", name)

btn = tk.Button(root, text="Submit", command=show_name)
btn.pack()

root.mainloop()
