import tkinter
import tkinter.messagebox
from tkinter import *
import tkinter.font as font
window=tkinter.Tk()


def nextr():
    window.destroy()
    import sudoku
def nextw():
    window.destroy()
    import rules

window.title("Number Master")

#main screen
window.configure(bg='#A9A9A9')
#Setting font size
myFont = font.Font(family = "Cambria",size=25,weight='bold')
myFont1 = font.Font(family = "Georgia",size=30,weight='bold')
#headings
var=tkinter.Label(window,text="NUMBER MASTER",bg='#29C5F6',fg='white')

#buttons
Btn=tkinter.Button(window,text='Get Started',command=nextr ,bg="#FFEBCD",bd=0.3)
Btn2=tkinter.Button(window,text='Rules',command=nextw ,bg="#FFEBCD",bd=0.3)
Btn3=tkinter.Button(window,text='Quit',command=window.destroy,bg="#FFEBCD",bd=0.3)



var['font'] = myFont1
Btn['font'] = myFont
Btn2['font']= myFont
Btn3['font']= myFont

#Setting Positions of buttons and heading

var.place(relx=0.5, rely=0.1, anchor=CENTER)
Btn.place(relx=0.5, rely=0.3, anchor=CENTER)
Btn2.place(relx=0.5, rely=0.5, anchor=CENTER)
Btn3.place(relx=0.5, rely=0.7, anchor=CENTER)



#setting Window's geometry
window.geometry("500x600")
window.mainloop()
