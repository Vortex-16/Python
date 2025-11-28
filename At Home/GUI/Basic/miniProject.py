import tkinter as tk

root = tk.Tk()
root.geometry("400x350")
root.title("Login Form")

frame = tk.Frame(root, padx=20, pady=20, bd=2, relief="groove")
username_label = tk.Label(frame, text="Username:", font=("Arial", 14))
username_label.grid(row=0, column=0, pady=10, sticky="w")

username_entry = tk.Entry(frame, font=("Arial", 14))
username_entry.grid(row=0, column=1, pady=10)
password_label = tk.Label(frame, text="Password:", font=("Arial", 14))
password_label.grid(row=1, column=0, pady=10, sticky="w")

password_entry = tk.Entry(frame, font=("Arial", 14), show="*")
password_entry.grid(row=1, column=1, pady=10)

login_btn = tk.Button(frame, text="Login", font=("Arial", 14), width=12)
login_btn.grid(row=2, column=0, columnspan=2, pady=20)

frame.pack(pady=40)

root.mainloop()
