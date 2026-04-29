import tkinter as tk
root=tk.Tk()
root.title('My App')
root.geometry('300x200')

label=tk.Label(root,text='hello, tkinter!')#label=object,Label=class,pack=method
label.pack(pady=20)

button=tk.Button(root,text='Exit', command=root.destroy) 
button.pack()

root.mainloop()