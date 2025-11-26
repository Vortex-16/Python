# A simple calculotor using tkinter and basic arithmetic operations (ask the user for input 1 and input 2 then arithmetic oprtaion to be performed and the display the reult in static so that it cant be modified by the user.).

import tkinter as tk
import customtkinter as ctk
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")
app = ctk.CTk()
app.title("vOS Calculator")
app.geometry("360x520")
app.minsize(360, 520)
app.maxsize(360, 520)
app.configure(fg_color="#E8E8E8")
frame = ctk.CTkFrame(app, corner_radius=25, fg_color="#F0F0F0")
frame.pack(padx=20, pady=20, fill="both", expand=True)
entry = ctk.CTkEntry(frame, width=300, height=70, 
                     corner_radius=20,
                     font=("Arial Rounded MT Bold", 28),
                     fg_color="#FFFFFF",
                     border_color="#DDDDDD",
                     border_width=2)
entry.pack(pady=20) 
buttons = [
    ['7','8','9','/'],
    ['4','5','6','*'],
    ['1','2','3','-'],
    ['0','.','=','+']
]
def click(value):
    if value == "=":
        try:
            res = str(eval(entry.get()))
            entry.delete(0, "end")
            entry.insert("end", res)
        except:
            entry.delete(0, "end")
            entry.insert("end", "Error")
    else:
        entry.insert("end", value)
for row_vals in buttons:
    row = ctk.CTkFrame(frame, fg_color="transparent")
    row.pack(pady=5)
    for val in row_vals:
        btn = ctk.CTkButton(
        row,
        text=val,
        width=65,
        height=65,
        corner_radius=20,
        font=("Arial Rounded MT Bold", 22),
        fg_color="#D9D9D9",
        command=lambda v=val: click(v)
        )
        btn.pack(side="left", padx=5)
app.mainloop()
        