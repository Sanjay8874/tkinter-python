from tkinter import*
root = Tk()
label = Label(root,text = "Enter your expression")
label.pack()

def evaluate(event):
    data = e.get()
    ans.configure(text="Answer:"+str(eval(data)))
e = Entry(root)

e.bind("<Return>",evaluate)
e.pack()
ans = Label(root)
ans.pack()
root.mainloop()

