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

app.mainloop()
