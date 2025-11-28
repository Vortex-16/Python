import tkinter as tk

root = tk.Tk()
root.geometry("400x300")

entry = tk.Entry(root, font=("Arial", 14))
entry.pack()

def say_hello():
    value= entry.get()
    print("You entered:", value)

btn = tk.Button(root, text="Click Me", command=say_hello)
btn.pack()

root.mainloop()

