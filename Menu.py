from tkinter import*

root = Tk()

def random():
    print("This is statement")

mainMenu = Menu(root)
root.configure(menu = mainMenu)

subMenu = Menu(mainMenu)
subMenu1 = Menu(mainMenu)

mainMenu.add_cascade(label="File",menu=subMenu)
subMenu.add_command(label="New File",command=random)
subMenu.add_command(label="Open",command=random)
subMenu.add_command(label="Open Module",command=random)
subMenu.add_command(label="Recent File",command=random)
subMenu.add_command(label="Save",command=random)
subMenu.add_command(label="Save as",command=random)


mainMenu.add_cascade(label="Edit",menu=subMenu1)
subMenu1.add_command(label="Undo",command=random)
subMenu1.add_command(label="Redo",command=random)
subMenu1.add_command(label="copy",command=random)
subMenu1.add_command(label="cut",command=random)
subMenu1.add_command(label="paste",command=random)



root.mainloop()
