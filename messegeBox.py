from tkinter import*
import tkinter.messagebox


root = Tk()

tkinter.messagebox.showinfo("Windw Title","Hello sanjay What are you doing right now??")

answer = tkinter.messagebox.askquestion("Question 1","Are you stand in college?")
if answer == "yes":
    tkinter.messagebox.showinfo("Yes, I'm in college","Wait some moment I am comeing to meet you")

if answer == "no":
    tkinter.messagebox.showinfo("Ok","then I will meet you after some time at home")
root.mainloop()
