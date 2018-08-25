
from tkinter import*
import os
import pymysql
from PIL import ImageTk,Image
def open_main():
    os.system('main_page.py')

def add_student():
    rollnum=rnum.get()
    stdname=sname.get()
    faname=fanm.get()
    mname=mtnm.get()
    dobr=dateob.get()
    brnch=bran.get()
    try:
        conn = pymysql.connect(host='localhost', user='root', password='', db='data')
        a = conn.cursor()
        a.execute("insert into student (rollno,studname,fathername,mothername,dob,branch)values('"+rollnum+"', '"+stdname+"', '"+faname+"', '"+mname+"', '"+dobr+"', '"+ brnch+"')")
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
load = Image.open('add.png')
render = ImageTk.PhotoImage(load)
img = Label(win, image=render)
img.image = render
img.place(x=0, y=0)

#middle frame
mframe=Frame(win,bg="brown",bd=10,relief='raise', padx=50, pady=30)
mframe.pack(padx=50,pady=50)

lbl1 = Label(mframe,font=('arial',14,'bold'), bg='brown', text='Roll Number :')
lbl1.grid(row=0, column=0)
rnum=StringVar()
e1 = Entry(mframe,textvariable=rnum)
e1.grid(row=0, column=1, padx=10)


lbl2 = Label(mframe, font=('arial',14,'bold'), bg='brown', text='Student Name :')
lbl2.grid(row=1, column=0, pady=10)
sname=StringVar()
e2 = Entry(mframe,textvariable=sname)
e2.grid(row=1, column=1, padx=10)

lbl3 = Label(mframe, font=('arial',14,'bold'), bg='brown', text='Fathers Name :')
lbl3.grid(row=2, column=0, pady=10)

fanm=StringVar()
e3 = Entry(mframe,textvariable=fanm)
e3.grid(row=2, column=1, padx=10)

lbl4 = Label(mframe, font=('arial',14,'bold'), bg='brown', text='Mother Name :')
lbl4.grid(row=3, column=0, pady=10)
mtnm=StringVar()
e4 = Entry(mframe,textvariable=mtnm)
e4.grid(row=3, column=1, padx=10)

lbl5 = Label(mframe, font=('arial',14,'bold'), bg='brown', text='Date of Birth :')
lbl5.grid(row=4, column=0, pady=10)
dateob=StringVar()
e5 = Entry(mframe,textvariable=dateob)
e5.grid(row=4, column=1, padx=10)

lbl6 = Label(mframe, font=('arial',14,'bold'), bg='brown', text='Branch')
lbl6.grid(row=5, column=0, pady=10)
bran=StringVar()
e6 = Entry(mframe,textvariable=bran)
e6.grid(row=5, column=1, padx=10)

mframe.pack(padx=50,pady=20)
exitmain = Button(mframe, font=('arial',14,'bold'), bg='brown',text='GO TO Main',fg="pink",command=open_main)
exitmain.grid(row=6, column=0, padx=10)
closemain = Button(mframe, font=('arial',14,'bold'), bg='brown',text='Close',fg="pink",command=win.destroy)
closemain.grid(row=6, column=2, padx=10)


e3 = Button(mframe, font=('arial',14,'bold'), bg='brown',text='Add Student',fg="pink",command=add_student)
e3.grid(row=6, column=1, padx=10)

win.mainloop()
