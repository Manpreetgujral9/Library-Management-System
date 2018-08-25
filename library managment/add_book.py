from  tkinter import *
import os
def open_main():
    os.system('main_page.py')
import pymysql
from PIL import ImageTk,Image
def add_book():
    bkname=booknm.get()
    bknum=booknum.get()
    try:
        conn = pymysql.connect(host='localhost', user='root', password='', db='data')
        a = conn.cursor()
        a.execute("insert into books(bookname,bookno)values('"+bkname+"','"+bknum+"')")
        conn.commit()
        print('save')
    except:
        conn.rollback()
        print('Not Save')
        conn.close()
win=Tk()
win.overrideredirect(True)
win.overrideredirect(False)
win.attributes('-fullscreen',True)
win.title("windows application")
win.configure(bg='gray')
load = Image.open('img7.png')
render = ImageTk.PhotoImage(load)
img = Label(win, image=render)
img.image = render
img.place(x=0, y=0)

#middle frame
mframe=Frame(win,width=800,height=800,bg="brown",bd=10,relief='raise', padx=80)
mframe.pack(padx=50,pady=200)

lbl1 = Label(mframe, font=('arial',14,'bold'), bg='brown', text='Book Name :')
lbl1.grid(row=0, column=0)
booknm=StringVar()
e1 = Entry(mframe,textvariable=booknm)
e1.grid(row=0, column=1, padx=10, pady=10)

lbl2 = Label(mframe, font=('arial',14,'bold'), bg='brown', text='Book Number :')
lbl2.grid(row=1, column=0, pady=10)
booknum=StringVar()
e2 = Entry(mframe,textvariable=booknum)
e2.grid(row=1, column=1, padx=10)

exitmain = Button(mframe, font=('arial',14,'bold'), bg='brown',text='GO TO Main',fg="pink",command=open_main)
exitmain.grid(row=2, column=0, padx=10)
closemain = Button(mframe, font=('arial',14,'bold'), bg='brown',text='Close',fg="pink",command=win.destroy)
closemain.grid(row=2, column=2, padx=10)

e3 = Button(mframe, text='Submit', font=('arial',14,'bold'),fg="white",bg="brown",command=add_book)
e3.grid(row=2, column=1, pady=10)

win.mainloop()
