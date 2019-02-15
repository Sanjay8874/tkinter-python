from tkinter import*

root = Tk()

def leftClick(event):
    print("Left")

def rightClick(event):
    print("Right")

def scroll(event):
    print("Scroll")

def leftKey(event):
    print("Left Key passed")

def rightKey(event):
    print("Right Key passed")      
          

root.geometry("500x500")
root.bind("<Button-1>",leftClick)
root.bind("<Button-2>",rightClick)
root.bind("<Button-3>",scroll)
root.bind("<Button-4>",leftKey)
root.bind("<Button-5>",rightKey)
root.mainloop()
