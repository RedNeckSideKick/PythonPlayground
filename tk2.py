import tkinter as tk
#import rgb

win = tk.Tk()
win.geometry("500x500")

def term():
    win.quit()
    win.destroy()

frame = tk.Frame(win,height=500,width=600)

menuButton = tk.Menubutton(frame,text="MENU")

menuButton.menu = tk.Menu(menuButton)
menuButton["menu"] = menuButton.menu

menuButton.menu.add_command(label="Quit",command=term)

frame.pack()
menuButton.pack()
menuButton.place(x=0,y=0,width=500)

win.mainloop()