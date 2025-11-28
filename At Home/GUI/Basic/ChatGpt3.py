import tkinter as tk

root = tk.Tk()
root.geometry("400x300")

def say_hello():
    print("Button clicked!")

btn = tk.Button(root, text="Click Me", command=say_hello)
btn.pack()

root.mainloop()
