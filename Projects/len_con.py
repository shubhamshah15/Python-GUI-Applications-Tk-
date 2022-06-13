from tkinter import *

App = Tk()
App.title("Length Converter")
scales = ['Meters', 'Inches', 'Foot']
App.geometry("300x200")

_from = StringVar()
from_scale = OptionMenu(App, _from, *scales)
from_scale.grid(row=0, column=0, pady=5)

lbl = Label(App, text=" convert to ")
lbl.grid(row=0, column=1, pady=5)

to_ = StringVar()
to_scale = OptionMenu(App, to_, *scales)
to_scale.grid(row=0, column=2, pady=5)

enterL = Label(App, text="Enter a length:")
enterL.grid(row=1, column=0, columnspan=2, pady=5)

numE = Entry(App, width=10)
numE.grid(row=1, column=2, columnspan=2, pady=5)


def converter():
    From = _from.get()
    To = to_.get()
    num = float(numE.get())
    
    if From == "Meters" and To == "Inches":
            conv_num = num * 39.37
    elif From == "Meters" and To == "Foot":
            conv_num = num * 3.28
    elif From == "Inches" and To == "Meters":
            conv_num = num / 39.37
    elif From == "Inches" and To == "Foot":
            conv_num = num / 12
    elif From == "Foot" and To == "Meters":
            conv_num = num / 3.28
    elif From == "Foot" and To == "Inches":
            conv_num = num * 12
    else:
            conv_num = num
            
    numL = Label(App, text=round(conv_num,2), width=10)
    numL.grid(row=1, column=4, pady=5)

ConvertB = Button(App, text="Convert", command=converter)
ConvertB.grid(row=2, column=0, pady=5)

App.mainloop()