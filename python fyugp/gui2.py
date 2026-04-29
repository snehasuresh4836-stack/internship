import tkinter as tk

root = tk.Tk()
root.title('My App')
import tkinter as tk

root = tk.Tk()
root.title('My App')
root.geometry('300x200')

# Labels
tk.Label(root, text='Name').grid(row=0, column=0, padx=10, pady=5)
tk.Label(root, text='Email').grid(row=1, column=0, padx=10, pady=5)
tk.Label(root, text='Mobile').grid(row=2, column=0, padx=10, pady=5)

# Entry fields
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

email_entry = tk.Entry(root)
email_entry.grid(row=1, column=1, padx=10, pady=5)

mobile_entry = tk.Entry(root)
mobile_entry.grid(row=2, column=1, padx=10, pady=5)

# Function
def submit():
    print("Name:", name_entry.get())
    print("Email:", email_entry.get())
    print("Mobile:", mobile_entry.get())

# Buttons
tk.Button(root, text='Submit', command=submit).grid(row=3, column=0, pady=10)
tk.Button(root, text='Exit', command=root.destroy).grid(row=3, column=1)

root.mainloop()