from  tkinter import *
from tkinter import messagebox
import os
def open_main():
    os.system('main_page.py')
import pymysql
from PIL import ImageTk,Image
def delete():
    rollnum = rnum.get()

    try:
        conn=pymysql.connect(host='localhost',user='root',password='',db='data')
        a=conn.cursor()
        a.execute("delete from student where rollno='"+rollnum+"'")
        conn.commit()
        # print('delete')
        messagebox.showinfo("message","delete")
    except:
        conn.rollback()
        # print('not delete')
        messagebox.showinfo("message","not delete")
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
mframe=Frame(win,width=800,height=800,bg="brown",bd=10,relief='raise', padx=40, pady=30)

lbl1 = Label(mframe, font=('arial',14,'bold'), bg='brown', text='Roll Number :')
lbl1.grid(row=0, column=0)
rnum=StringVar()
e1 = Entry(mframe,textvariable=rnum)
e1.grid(row=0, column=1, padx=10)

exitmain = Button(mframe, font=('arial',14,'bold'), bg='brown',text='GO TO Main',fg="pink",command=open_main)
exitmain.grid(row=2, column=0, padx=10)
e3 = Button(mframe, text='Delete', font=('arial',14,'bold'),fg="pink",bg="brown",command=delete)
e3.grid(row=2, column=1, pady=10)
closemain = Button(mframe, font=('arial',14,'bold'), bg='brown',text='Close',fg="pink",command=win.destroy)
closemain.grid(row=2, column=2, padx=10)

mframe.pack(padx=50,pady=20)

win.mainloop()
