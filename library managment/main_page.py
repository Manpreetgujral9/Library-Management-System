import tkinter as tk
from  tkinter import *
from PIL import ImageTk,Image
import os

def open_return():
    os.system('return.py')
def open_add():
    os.system('add_student.py')
def open_issue():
    os.system('Issue_book_page.py')
def open_delete():
    os.system('delete_stu.py')
def open_book():
    os.system('add_book.py')
def open_details():
    os.system('Student_details.py')


win=Tk()
win.overrideredirect(True)
win.overrideredirect(False)
win.attributes('-fullscreen',True)
win.title("windows application")
win.configure(bg='gray')
load = Image.open('img11.png')
render = ImageTk.PhotoImage(load)
img = Label(win, image=render)
img.image = render
img.place(x=0, y=0)
#Top Frame
topframe=Frame(win,width=4600,height=3500,bg="pink",bd=10,relief="raise")
topframe.pack(side=TOP)
lb=Label(topframe,font=('arial',45,'bold'),fg="pink",bg="brown",text='WELCOME', width=30)
lb.grid(row=0,column=0)

#middle frame
mframe=Frame(win,bg="brown",bd=10,relief='raise', padx=100, width=4600, height=3500)
mframe.pack(padx=150,pady=150)

lbl1 = Label(mframe,font=('arial',20,'bold'), text='Enter the Options to Pull The Records', bg="brown", fg='white')
lbl1.grid(row=0, columnspan=2)

e4 = Button(mframe, text='Add Student', font=('arial',14,'bold'),bg="brown",command=open_add)
e4.grid(row=4, column=0, pady=10)

e4 = Button(mframe, text='Issue Book', font=('arial',14,'bold'),bg="brown",command=open_issue)
e4.grid(row=4, column=1, pady=10)

e4 = Button(mframe, text='Return Book', font=('arial',14,'bold'),bg="brown",command=open_return)
e4.grid(row=5, column=0, pady=10)

e4 = Button(mframe, text='Add Book', font=('arial',14,'bold'),bg="brown",command=open_book)
e4.grid(row=5, column=1, pady=10)

e4 = Button(mframe, text='View Student Details', font=('arial',14,'bold'),bg="brown",command=open_details)
e4.grid(row=6, column=0, pady=10)

e4 = Button(mframe, text='Delete Student', font=('arial',14,'bold'),bg="brown",command=open_delete)
e4.grid(row=6, column=1, pady=10)
closemain = Button( font=('arial',14,'bold'), bg='brown',text='Close Main',fg="pink",command=win.destroy)
closemain.pack(side=BOTTOM)

win.mainloop()
