from  tkinter import *
from PIL import ImageTk,Image
import os
def open_main():
    os.system('main_page.py')
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
mframe=Frame(win,width=800,height=800,bg="brown",bd=10,relief='raise', padx=40, pady=30)
mframe.pack(padx=50,pady=70)

lbl1 = Label(mframe, font=('arial',14,'bold'), bg="brown", text='Book Number :')
lbl1.grid(row=0, column=0)

e1 = Entry(mframe)
e1.grid(row=0, column=1, padx=10)

exitmain = Button(mframe, font=('arial',14,'bold'), bg='brown',text='GO TO Main',fg="pink",command=open_main)
exitmain.grid(row=3, column=0, padx=10)
closemain = Button(mframe, font=('arial',14,'bold'), bg='brown',text='Close',fg="pink",command=win.destroy)
closemain.grid(row=3, column=2, padx=10)


e3 = Button(mframe, text='Submit', font=('arial',14,'bold'),fg="pink",bg="brown")
e3.grid(row=3, column=1, pady=10)


win.mainloop()
