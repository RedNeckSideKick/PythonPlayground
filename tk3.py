import tkinter as tk
from tkinter import messagebox

win = tk.Tk()
#win.geometry("500x500")

def term():
    win.quit()
    win.destroy()
    
def callback():
    print("Callback entered")
    
def info():
    messagebox.showinfo(title="Info",message="""\
    Tk test program # 3!
    """,detail="""\
    Wheee!
    """)

menu = tk.Menu(win)
win.config(menu=menu)

filemenu = tk.Menu(menu)
menu.add_cascade(label="File", menu=filemenu)

filemenu.add_command(label="New", command=callback)
filemenu.add_command(label="Open", command=callback)
filemenu.add_command(label="Save", command=callback)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=term)

editmenu = tk.Menu(menu)
menu.add_cascade(label="Edit", menu=editmenu)

editmenu.add_command(label="Undo",command=callback)
editmenu.add_command(label="Redo",command=callback)
editmenu.add_separator()
editmenu.add_command(label="Cut",command=callback)
editmenu.add_command(label="Copy",command=callback)
editmenu.add_command(label="Paste",command=callback)
editmenu.add_separator()
editmenu.add_command(label="Delete",command=callback)

helpmenu = tk.Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)

helpmenu.add_command(label="About", command=info)

win.mainloop()

