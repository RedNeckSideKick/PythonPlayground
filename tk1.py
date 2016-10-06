import tkinter as tk
#import rgb

win = tk.Tk(screenName="My Program")
win.geometry("600x500")

def fn():
    print("Hello!")

frame = tk.Frame(win,height=500,width=600)

quitButton = tk.Button(frame,text="Quit",fg="red",command=win.destroy)

canvas = tk.Canvas(frame,height=500,width=500)

box = (2,2,500,500)
#color = (100,150,200)
filename = tk.BitmapImage(file = 'pixels.bmp')

#circle = canvas.create_oval(box,fill=rgb.rgb(100,150,200))
image = canvas.create_image(50, 50, anchor=NE, image=filename)

frame.pack()

quitButton.pack()
quitButton.place(height=500,width=98,x=502,y=0)

canvas.pack()
canvas.place(x=0,y=0)

win.mainloop()