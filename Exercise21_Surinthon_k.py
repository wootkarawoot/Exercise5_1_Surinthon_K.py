from tkinter import *
import math
def leftClickButton(event):

    result = float(TextWeight.get()) / math.pow((float(TextHeight.get()) / 100), 2)

    if result >= 30.0:
        Textresult.configure(text="อ้วนมาก")
    elif result >= 25.0:
        Textresult.configure(text="อ้วน")
    elif result >= 23.0:
        Textresult.configure(text="น้ำหนักเกิน")
    elif result >= 18.6:
        Textresult.configure(text="น้ำหนักปกติ")
    else:
        Textresult.configure(text="ผอมเกินไป")


MainWindow = Tk()
labelHeight = Label(MainWindow,text="ส่วนสูง (Cm.)")
labelHeight.grid(row=0,column=0)

TextHeight = Entry(MainWindow)
TextHeight.grid(row=0,column=1)
labelWeight = Label(MainWindow,text="น้ำหนัก (Kg.)")
labelWeight.grid(row=1,column=0)

TextWeight = Entry(MainWindow)
TextWeight.grid(row=1,column=1)

calculateButton = Button(MainWindow,text="คำนวน")
calculateButton.bind('<Button-1>',leftClickButton)
calculateButton.grid(row=2,column=0)

Textresult = Label(MainWindow,text='น้ำหนักของคุณ..')
Textresult.grid(row= 2,column=1)

MainWindow.mainloop()
