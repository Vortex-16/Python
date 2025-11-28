import customtkinter as ctk

ctk.set_appearance_mode("light")  
ctk.set_default_color_theme("blue")  

app = ctk.CTk()
app.title("alphaOS Calculator")
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
        hover_color="#464646",
        text_color="black",
        command=lambda x=val: click(x)
        )
        btn.pack(side="left", padx=8)


bottom_row = ctk.CTkFrame(frame, fg_color="transparent")
bottom_row.pack(pady=15, fill="x")


clear_btn = ctk.CTkButton(
    bottom_row,
    text="Clear",
    width=140,           
    height=60,
    corner_radius=20,
    font=("Arial Rounded MT Bold", 22),
    fg_color="#FA4137",
    hover_color="#E0483D",
    command=lambda: entry.delete(0, "end")
)
clear_btn.pack(side="left", padx=10, expand=True)

equal_btn = ctk.CTkButton(
    bottom_row,
    text="=",
    width=140,          
    height=60,
    corner_radius=20,
    font=("Arial Rounded MT Bold", 22),
    fg_color="#5FFF5C",
    hover_color="#53CF3A",
    command=lambda: click("=")
)
equal_btn.pack(side="right", padx=10, expand=True)


app.mainloop()
