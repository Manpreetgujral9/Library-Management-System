from  tkinter import *
from tkinter import messagebox

import pymysql
from PIL import ImageTk,Image
import os
def open_main():
    os.system('main_page.py')
def issue_book():
    rollnum = rnum.get()
    bkname=booknm.get()
    bknum=booknum.get()
    datofiss=dateofiss.get()
    lastdateret=lstdate.get()


    try:
        conn = pymysql.connect(host='localhost', user='root', password='', db='data')
        a = conn.cursor()
        a.execute("insert into issuebook(rollno,bookname,bookno,issuedate,returndate)values('"+rollnum+"','"+bkname+"','"+bknum+"','"+datofiss+"','"+lastdateret+"')")
        conn.commit()
        print('save')
        messagebox.showinfo("Book Issued")
    except:
        conn.rollback()
        print('Not Save')
        messagebox.showinfo("Book Not Issued")
        conn.close()
win=Tk()
win.overrideredirect(True)
win.overrideredirect(False)
win.attributes('-fullscreen',True)
win.title("windows application")
win.configure(bg='gray')
load = Image.open('imgg.png')
render = ImageTk.PhotoImage(load)
img = Label(win, image=render)
img.image = render
img.place(x=0, y=0)


#middle frame
mframe=Frame(win,width=800,height=800,bg="brown",bd=10,relief='raise', padx=50, pady=30)
mframe.pack(padx=50,pady=100)

lbl1 = Label(mframe, font=('arial',14,'bold'), bg="brown", text='Roll Number :')
lbl1.grid(row=0, column=0)
rnum=StringVar()
e1 = Entry(mframe,textvariable=rnum)
e1.grid(row=0, column=1, padx=10)

lbl2 = Label(mframe, font=('arial',14,'bold'), bg="brown", text='Book Name :')
lbl2.grid(row=1, column=0, pady=10)
booknm=StringVar()
e2 = Entry(mframe,textvariable=booknm)
e2.grid(row=1, column=1, padx=10)

lbl3 = Label(mframe, font=('arial',14,'bold'), bg="brown", text='Book Number :')
lbl3.grid(row=2, column=0, pady=10)
booknum=StringVar()
e3 = Entry(mframe,textvariable=booknum)
e3.grid(row=2, column=1, padx=10)

lbl4 = Label(mframe, font=('arial',14,'bold'), bg="brown", text='Date of Issue :')
lbl4.grid(row=3, column=0, pady=10)
dateofiss=StringVar()
e4 = Entry(mframe,textvariable=dateofiss)
e4.grid(row=3, column=1, padx=10)

lbl5 = Label(mframe, font=('arial',14,'bold'), bg="brown", text='Last Date to return :')
lbl5.grid(row=4, column=0, pady=10)
lstdate=StringVar()
e5 = Entry(mframe,textvariable=lstdate)
e5.grid(row=4, column=1, padx=10)

exitmain = Button(mframe, font=('arial',14,'bold'), bg='brown',text='GO TO Main',fg="pink",command=open_main)
exitmain.grid(row=5, column=0, padx=10)
closemain = Button(mframe, font=('arial',14,'bold'), bg='brown',text='Close',fg="pink",command=win.destroy)
closemain.grid(row=5, column=2, padx=10)

e6 = Button(mframe, text='Submit', font=('arial',14,'bold'), bg="brown",command=issue_book)
e6.grid(row=5, column=1, pady=10)


win.mainloop()
