import tkinter
from tkinter import*
import os
from tkinter import messagebox

import pymysql
from PIL import ImageTk,Image
def open_main():
    os.system('main_page.py')

def details():
    rollnum = rnum.get()
    print(rollnum)
    conn = pymysql.connect(host='localhost', user='root', password='', db='data')
    a = conn.cursor()

    a.execute("select * from student where rollno='"+rollnum+"'")

    results = a.fetchall()

    count = a.rowcount

    print(results)

    print(count)

    if count > 0:
        for row in results:
            rnum1.set(row[0])
            sname.set(row[1])
            fanm.set(row[2])
            mtnm.set(row[3])
            dateob.set(row[4])
            bran.set(row[5])
    else:
        messagebox.showinfo("record not found")
    conn.close()





def bookdetails():
    rollnum = rnum.get()
    print(rollnum)
    conn = pymysql.connect(host='localhost', user='root', password='', db='data')
    b = conn.cursor()
    b.execute("select * from issuebook where rollno='" + rollnum + "'")
    resultb = b.fetchall()
    countb = b.rowcount
    print(resultb)
    print(countb)
    if countb > 0:
        for row in resultb:
            booknm.set(row[1])
            booknum.set(row[2])
            dateofiss.set(row[3])
            lstdate.set(row[4])

    else:
        messagebox.showinfo("record not found")
    conn.close()
def details_and_bookdetails():
    details()
    bookdetails()
win=Tk()
win.overrideredirect(True)
win.overrideredirect(False)
win.attributes('-fullscreen',True)
win.title("windows application")
win.configure(bg='gray')
load = Image.open('add.png')
render = ImageTk.PhotoImage(load)
img = Label(win, image=render)
img.image = render
img.place(x=0, y=0)
#top frame
topframe=Frame(win,width=4600,height=3500,bg="pink",bd=10,relief="raise")
topframe.pack(side=TOP)
lb=Label(topframe,font=('arial',45,'bold'),fg="pink",bg="brown",text='Students Detail', width=30)
lb.grid(row=0,column=0)

rframe=Frame(win,bg="brown",bd=10,relief='raise', padx=10, pady=10)
rframe.pack(padx=5,pady=5)
labelroll = Label(rframe,font=('arial',14,'bold'), bg='brown', text='Enter Roll Number :')
labelroll.grid(row=0, column=0)
rnum=StringVar()
r1 = Entry(rframe,textvariable=rnum)
r1.grid(row=0, column=1, padx=10)

roll3 = Button(rframe, text='Submit', font=('arial',14,'bold'),fg="white",bg="brown",command=details_and_bookdetails)
roll3.grid(row=0, column=2, pady=10)
#middle frame

mframe=Frame(win,bg="brown",bd=10,relief='raise', padx=20, pady=10)
mframe.pack(padx=5,pady=10)
lbl1 = Label(mframe,font=('arial',14,'bold'), bg='brown', text='Roll Number :')
lbl1.grid(row=1, column=0)
rnum1=StringVar()
e1 = Entry(mframe,textvariable=rnum1)
e1.grid(row=1, column=1, padx=10)


lbl2 = Label(mframe, font=('arial',14,'bold'), bg='brown', text='Student Name :')
lbl2.grid(row=2, column=0, pady=10)
sname=StringVar()
e2 = Entry(mframe,textvariable=sname)
e2.grid(row=2, column=1, padx=10)

lbl3 = Label(mframe, font=('arial',14,'bold'), bg='brown', text='Fathers Name :')
lbl3.grid(row=3, column=0, pady=10)

fanm=StringVar()
e3 = Entry(mframe,textvariable=fanm)
e3.grid(row=3, column=1, padx=10)

lbl4 = Label(mframe, font=('arial',14,'bold'), bg='brown', text='Mother Name :')
lbl4.grid(row=4, column=0, pady=10)
mtnm=StringVar()
e4 = Entry(mframe,textvariable=mtnm)
e4.grid(row=4, column=1, padx=10)

lbl5 = Label(mframe, font=('arial',14,'bold'), bg='brown', text='Date of Birth :')
lbl5.grid(row=5, column=0, pady=10)
dateob=StringVar()
e5 = Entry(mframe,textvariable=dateob)
e5.grid(row=5, column=1, padx=10)

lbl6 = Label(mframe, font=('arial',14,'bold'), bg='brown', text='Branch')
lbl6.grid(row=6, column=0, pady=10)
bran=StringVar()
e6 = Entry(mframe,textvariable=bran)
e6.grid(row=6, column=1, padx=10)

sideframe=Frame(win,bg="brown",bd=10,relief='raise', padx=20, pady=10)
sideframe.pack(padx=5,pady=10)
lbs1 = Label(mframe, font=('arial',14,'bold'), bg="brown", text='Book Name :')
lbs1.grid(row=7, column=0, pady=10)
booknm=StringVar()
s1 = Entry(mframe,textvariable=booknm)
s1.grid(row=8, column=0, padx=10)

lbs2 = Label(mframe, font=('arial',14,'bold'), bg="brown", text='Book Number :')
lbs2.grid(row=7, column=1, pady=10)
booknum=StringVar()
s2 = Entry(mframe,textvariable=booknum)
s2.grid(row=8, column=1, padx=10)

lbs3 = Label(mframe, font=('arial',14,'bold'), bg="brown", text='Date of Issue :')
lbs3.grid(row=7, column=2, pady=10)
dateofiss=StringVar()
s3 = Entry(mframe,textvariable=dateofiss)
s3.grid(row=8, column=2, padx=10)

lbs4= Label(mframe, font=('arial',14,'bold'), bg="brown", text='Last Date to return :')
lbs4.grid(row=7, column=3, pady=10)
lstdate=StringVar()
s4 = Entry(mframe,textvariable=lstdate)
s4.grid(row=8, column=3, padx=10)

mframe=Frame(win,bg="brown",bd=10,relief='raise', padx=50, pady=30)
mframe.pack(padx=50,pady=20)
closemain = Button(mframe, font=('arial',14,'bold'), bg='brown',text='Close',fg="pink",command=win.destroy)
closemain.grid(row=2, column=1, padx=10)

exitmain = Button(mframe, font=('arial',14,'bold'), bg='brown',text='GO TO Main',fg="pink",command=open_main)
exitmain.grid(row=2, column=0, padx=10)
win.mainloop()
