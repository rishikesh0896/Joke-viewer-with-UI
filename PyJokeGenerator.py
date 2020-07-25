from tkinter import *
import pyjokes as pj
root = Tk()
choice=Label(root, text="Select Your Choice :").place(x=365,y=0)
root.title('PyJoke Viewer')
root.geometry('1000x175')
clicked=StringVar(root)
clicked.set('neutral')
drop=OptionMenu(root,clicked,'neutral','all','chuck')
drop.place(x=500,y=0)
e=Entry(root,width=162,borderwidth=1)
e.place(x=10,y=100)

def GenerateJokes():
    clicked1=clicked.get()
    joke=pj.get_joke('en',clicked1)
    e.insert(0,joke)

def clear_joke():
     e.delete(0,END)    
button = Button(root, text="Click to LOL", padx=10, pady=5,command=GenerateJokes)
button_clr=Button(root,text='Clear',padx=15,pady=4,command=clear_joke)
button.place(x=400,y=45)
button_clr.place(x=570,y=45)
root.mainloop()
