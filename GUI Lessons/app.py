from tkinter import *
from random import sample,choice


App = Tk()
App.title('Element Picker')
App.geometry('220x180')
# App['background'] = 'grey'

inp = Entry(App)
inp.grid(row=0, column=0, columnspan=2, padx=25, pady=5)

# Checkbox Code

# chk = Checkbutton(App, text='Double', variable=no_choice, onvalue=2, offvalue=1)
# chk.grid(row=1, column=0, columnspan=2, padx=25, pady=5)
# chk.deselect()

# Radio button Code

# rb1 = Radiobutton(App, text='1', variable=no_choice, value='1')
# rb2 = Radiobutton(App, text='2', variable=no_choice, value='2')
# rb1.grid(row=1, column=0, columnspan=1, padx=25, pady=5)
# rb2.grid(row=2, column=0, columnspan=1, padx=25, pady=5)
# rb1.select()
# rb2.deselect()

# Slider Code
no_choice = IntVar()
sld = Scale(App, from_=1, to=5, variable=no_choice, orient=HORIZONTAL)
sld.grid(row=1, column=0, columnspan=2, padx=25, pady=5)


def pick():
    INP = (inp.get()).split(',')
    
    if no_choice.get() != 1:
        ele = sample(INP, no_choice.get())
        lbl = ''
        for e in ele:
            lbl += ' ' + e
        ch = 'Choice: ' + str(lbl)
    else:
        ch = 'Choice: ' + str(choice(INP))
    
    OutWin = Toplevel()
    OutWin.title("Output")
    
    msg = Label(OutWin, text=ch, width=25)
    msg.grid(row=3, column=0, columnspan=2, padx=25, pady=5)
    
    if quitB['state'] == DISABLED:
        quitB['state'] = NORMAL

B = Button(App, text='Choose', command=pick)
B.grid(row=2, column=0, padx=25, pady=5)

quitB = Button(App, text='Cancel', command=App.quit, state=DISABLED)
quitB.grid(row=2, column=1, padx=25, pady=5)

App.mainloop()