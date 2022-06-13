from cProfile import label
from tkinter import *
from datetime import *

bg = 'black'
fg = 'cyan'

App = Tk()
App.title("Age Calculator")
App['background'] = bg
App.geometry("400x200")

msg = Label(App, text="Enter your DOB:", background=bg, foreground=fg)
msg.grid(row=0, column=0, columnspan=3)

dayL = Label(App, text="Day: ", background=bg, foreground=fg)
dayE = Entry(App, width=3, background=bg, foreground=fg)

monthL = Label(App, text=" Month: ", background=bg, foreground=fg)
monthE = Entry(App, width=3, background=bg, foreground=fg)

yearL = Label(App, text=" Year: ", background=bg, foreground=fg)
yearE = Entry(App, width=4, background=bg, foreground=fg)

dayL.grid(row=1, column=0)
dayE.grid(row=1, column=1)
monthL.grid(row=1, column=2)
monthE.grid(row=1, column=3)
yearL.grid(row=1, column=4)
yearE.grid(row=1, column=5)


def find_days():
    date = int(dayE.get())
    month = int(monthE.get())
    year = int(yearE.get())
    dob = datetime(day=date, month=month, year=year)
    
    time_now = datetime.now()
    time_diff = time_now - dob
    
    dys = Label(App, text="You lived " + str(time_diff.days) + " days!", background=bg, foreground=fg)
    dys.grid(row=3, column=0, columnspan=4)

def find_secs():
    date = int(dayE.get())
    month = int(monthE.get())
    year = int(yearE.get())
    dob = datetime(day=date, month=month, year=year)
    
    time_now = datetime.now()
    time_diff = time_now - dob
    
    secs = Label(App, text="You lived " + str(time_diff.total_seconds()) + " seconds!", background=bg, foreground=fg)
    secs.grid(row=4, column=0, columnspan=4)

totalD = Button(App, text="Total Days", command=find_days, background=bg, foreground=fg)
totalD.grid(row=2, column=0, columnspan=3)

totalS = Button(App, text="Total Seconds", command=find_secs, background=bg, foreground=fg)
totalS.grid(row=2, column=3, columnspan=3)

App.mainloop()