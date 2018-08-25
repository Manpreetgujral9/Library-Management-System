from  tkinter import *
import os
from tkinter import messagebox


def open_main():
    os.system('main_page.py')
import pymysql
from PIL import ImageTk,Image
def login():
    us = user.get()
    ps = pswd.get()
    conn = pymysql.connect(host='localhost', user='root', password='', db='data')
    a = conn.cursor()
    a.execute("select * from login where username='" + us + "' and password = '"+ps+"'")
    results = a.fetchall()
    count = a.rowcount
    print(results)
    print(count)
    if count > 0:

        os.system('main_page.py')
        # welcome.configure(bg = 'grey')
        # welcome.geometry('1000x1400')
        # l = Label(welcome, text='Book Library Management', font=('arial', 80, 'bold'), fg='red', bg='black', bd=10,
        #           relief='ridge')
        # l.grid(row=0, ipadx=100)
        #
        # lb = Label(welcome, text='Welcome! Login successfull', font=('arial', 50, 'bold'), fg='pink')
        # lb.grid(row=1, padx=30, pady=30, columnspan=3)
        #

    else:
        messagebox.showinfo("message","record not found")
    conn.close()

    
win=Tk()
win.overrideredirect(True)
win.overrideredirect(False)
win.attributes('-fullscreen',True)

win.title("windows application")
win.configure(bg='gray')
load = Image.open('admin2.png')
render = ImageTk.PhotoImage(load)
img = Label(win, image=render)
img.image = render
img.place(x=0, y=0)

#top frame
topframe=Frame(win,width=4600,height=3500,bg="pink",bd=10,relief="raise")
topframe.pack(side=TOP)
lb=Label(topframe,font=('arial',45,'bold'),fg="pink",bg="brown",text='BOOK LIBRARY MANAGEMENT', width=30)
lb.grid(row=0,column=0)

#middle frame
mframe=Frame(win,bg="brown",bd=10,relief='raise', padx=30, pady=100)
mframe.pack(padx=500,pady=40)

lbl1 = Label(mframe, text='User name',font=('arial',12,'bold'),fg="pink",bg="brown")
lbl1.grid(row=0, column=0,pady=10)
user=StringVar()
e1 = Entry(mframe,textvariable = user)
e1.grid(row=0, column=1, padx=10)

lbl2 = Label(mframe, text='Password',font=('arial',12,'bold'),fg="pink",bg="brown")
lbl2.grid(row=1, column=0, pady=10)
pswd=StringVar()
e2 = Entry(mframe,textvariable = pswd)
e2.grid(row=1, column=1, padx=10)

closemain = Button(mframe, font=('arial',12,'bold'), bg='brown',text='Close Main',fg="pink",command=win.destroy)
closemain.grid(row=2, column=0, padx=10)

e3 = Button(mframe, text='Log in', font=('arial',12,'bold'),fg="pink",bg="brown",command=login)
e3.grid(row=2, column=1, padx=10)



win.mainloop()













