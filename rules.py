import tkinter
import tkinter.messagebox
from tkinter import *
import tkinter.font as font
window=tkinter.Tk()
window.title("Number Master")

#main screen
window.configure(bg='#A9A9A9')
def nextr():
    window.destroy()
    import sudoku

def nextw():
    window.destroy()
    import mainframe

myFont = font.Font(family = "Cambria",size=10,weight='bold')

Btn=tkinter.Button(window,text='Start',command=nextr ,bg="#FFEBCD",bd=0.3)
Btn2=tkinter.Button(window,text='Back',command=nextw ,bg="#FFEBCD",bd=0.3)


#Setting font size
var=tkinter.Label(window,text="NUMBER MASTER",bg='#29C5F6',fg='black')
var1=tkinter.Label(window,text="Rule No 1: Each row must contain the numbers from 1 to 9, without repetitions",bg='#29C5F6',fg='white')
var2=tkinter.Label(window,text="Rule No 2: Each column must contain the numbers from 1 to 9, without repetitions.",bg='#29C5F6',fg='white')
var3=tkinter.Label(window,text="Rule No 3: The digits(0,9) can only occur once per block ",bg='#29C5F6',fg='white')



var['font'] = myFont
var1['font'] = myFont
var2['font'] = myFont
var3['font'] = myFont



Btn['font'] = myFont
Btn2['font']= myFont

var.place(relx=0.5, rely=0.1, anchor=CENTER)
var1.place(relx=0.5, rely=0.3, anchor=CENTER)
var2.place(relx=0.5, rely=0.4, anchor=CENTER)
var3.place(relx=0.5, rely=0.5, anchor=CENTER)



Btn.place(relx=0.3, rely=0.8, anchor=CENTER)
Btn2.place(relx=0.7, rely=0.8, anchor=CENTER)
#setting Window's geometry
window.geometry("500x600")
window.mainloop()
