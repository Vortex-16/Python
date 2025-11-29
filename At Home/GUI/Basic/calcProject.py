import customtkinter as ctk

# Theme setup
ctk.set_appearance_mode("system")       # dark / light / system
ctk.set_default_color_theme("blue")   # blue / green / dark-blue

# Create window
app = ctk.CTk()
app.title("Modern Calculator")
app.geometry("360x520")
app.resizable(False, False)

display_var = ctk.StringVar(value="0")              # holds the text shown on the screen
display_entry = ctk.CTkEntry(app,
                             textvariable=display_var,
                             font=ctk.CTkFont(size=28, weight="bold"),
                             justify="right",
                             state="readonly",
                             width=320,
                             height=70)
display_entry.place(x=20, y=30) 
btn = ctk.CTkButton(app,
                    text="7",
                    corner_radius=40,   # makes it pill-shape
                    font=ctk.CTkFont(size=22, weight="bold"),
                    width=70,
                    height=70)
# ---------- BUTTON CLICK HANDLER ----------
def btn_click(value):
    current = display_var.get()
    if current == "0":
        display_var.set(value)
    else:
        display_var.set(current + value)

# ---------- BUTTONS FRAME ----------
btn_frame = ctk.CTkFrame(app)
btn_frame.place(x=20, y=130)
buttons = [
    ["C", "DEL", "%", "/"],
]

for r, row in enumerate(buttons):
    for c, value in enumerate(row):
        btn = ctk.CTkButton(btn_frame,
                            text=value,
                            corner_radius=40,
                            font=ctk.CTkFont(size=22, weight="bold"),
                            width=70,
                            height=70,
                            command=lambda v=value: btn_click(v))
        btn.grid(row=r, column=c, padx=5, pady=5)
buttons = [
    ["C", "DEL", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["00", "0", ".", "="]
]

for r, row in enumerate(buttons):
    for c, value in enumerate(row):
        btn = ctk.CTkButton(
            btn_frame,
            text=value,
            corner_radius=40,
            font=ctk.CTkFont(size=22, weight="bold"),
            width=70,
            height=70,
            command=lambda v=value: btn_click(v)
        )
        btn.grid(row=r, column=c, padx=5, pady=5)
def btn_click(value):
    current = display_var.get()

    # Clear (C)
    if value == "C":
        display_var.set("0")
        return

    # Delete last digit (DEL)
    if value == "DEL":
        if len(current) > 1:
            display_var.set(current[:-1])
        else:
            display_var.set("0")
        return

    # Evaluate (=)
    if value == "=":
        try:
            result = str(eval(current))
            display_var.set(result)
        except:
            display_var.set("Error")
        return

    # Normal input
    if current == "0":
        display_var.set(value)
    else:
        display_var.set(current + value)
def create_button(text):
    # operator buttons styling
    operators = {"/", "*", "-", "+", "%"}
    
    if text in operators:
        fg = "#1f6aa5"      # blue operator color
    elif text in {"C", "DEL"}:
        fg = "#a51f1f"      # red for clear/delete
    elif text == "=":
        fg = "#17981a"      # green for equals
    else:
        fg = "#2c2c2c"      # number buttons (dark gray)
    
    return ctk.CTkButton(
        btn_frame,
        text=text,
        corner_radius=40,
        font=ctk.CTkFont(size=22, weight="bold"),
        width=70,
        height=70,
        fg_color=fg,
        hover_color="#000000",
        command=lambda v=text: btn_click(v)
    )


app.mainloop()
