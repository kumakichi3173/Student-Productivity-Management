import tkinter as tk
from tkinter import messagebox # imports a messagebox

# creates the top level window
root = tk.Tk()
root.geometry('300x100')
root.title('Entry test')

# creates and places the Entry widget  
txt = tk.Entry(width=20)
txt.pack(pady=20)

#ハンドラ関数
def click():
    messagebox.showinfo(('message'), txt.get())

# creates and places the Button widget
btn = tk.Button(root, text = 'show', command = click)
btn.pack()

# shows the top level window
root.mainloop() 