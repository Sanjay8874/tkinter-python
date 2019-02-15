from tkinter import *
root = Tk()

Button1 = Button(None,text = "click!",fg = "blue")
Button1.pack()
Button2 = Button(None,text = "click!",fg = "red")
Button2.pack(fill = X)
Button3 = Button(None,text = "click!",fg = "purple")
Button3.pack()
Button4 = Button(None,text = "click!",fg = "Yellow")
Button4.pack(side = RIGHT,fill = Y)
root.mainloop()
