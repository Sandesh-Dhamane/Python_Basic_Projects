import tkinter as tk
from tkinter import messagebox

def generate_card():
    full_name = full_name_entry.get()
    age = age_entry.get()
    email = email_entry.get()
    company_name = company_name_entry.get()
    package = package_entry.get()
    do_you_work = work_var.get()

    message = f"Full Name: {full_name}\nAge: {age}\nEmail: {email}\nCompany Name: {company_name}\nPackage: {package}\nDo you work: {'Yes' if do_you_work else 'No'}"

    messagebox.showinfo("Generated Card", message)

root = tk.Tk()
root.title("User Form")

# Labels
tk.Label(root, text="Full Name:").grid(row=0, column=0, sticky="e", padx=10, pady=5)
tk.Label(root, text="Age:").grid(row=1, column=0, sticky="e", padx=10, pady=5)
tk.Label(root, text="Email:").grid(row=2, column=0, sticky="e", padx=10, pady=5)
tk.Label(root, text="Company Name:").grid(row=3, column=0, sticky="e", padx=10, pady=5)
tk.Label(root, text="Package:").grid(row=4, column=0, sticky="e", padx=10, pady=5)

# Entries
full_name_entry = tk.Entry(root)
age_entry = tk.Entry(root)
email_entry = tk.Entry(root)
company_name_entry = tk.Entry(root)
package_entry = tk.Entry(root)

full_name_entry.grid(row=0, column=1, sticky="w", padx=10, pady=5)
age_entry.grid(row=1, column=1, sticky="w", padx=10, pady=5)
email_entry.grid(row=2, column=1, sticky="w", padx=10, pady=5)
company_name_entry.grid(row=3, column=1, sticky="w", padx=10, pady=5)
package_entry.grid(row=4, column=1, sticky="w", padx=10, pady=5)

# Checkbox
work_var = tk.BooleanVar()
work_checkbox = tk.Checkbutton(root, text="Do you work?", variable=work_var)
work_checkbox.grid(row=5, columnspan=2, sticky="w", padx=10, pady=5)

# Button
generate_button = tk.Button(root, text="Generate Card", command=generate_card, bg="green")
generate_button.grid(row=6, columnspan=2, sticky="n", padx=10, pady=10)

root.mainloop()
