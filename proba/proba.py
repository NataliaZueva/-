from tkinter import *
from tkinter import ttk
 
clicks = 0
 
root = Tk()
root.title("Перевод валют")
root.geometry("400x300")
 
def clicked(event): 
    print("clicked")
 
btn = ttk.Button(text="Click")
btn.pack(anchor= S, expand=1)
 
# привязка события к кнопкам ttk.Button
root.bind_class("TButton", "<ButtonPress-1>", clicked)
 
root.mainloop()