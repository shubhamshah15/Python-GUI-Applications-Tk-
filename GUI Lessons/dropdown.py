from tkinter import *

App = Tk()

menu_choice = StringVar()
options = ['Red', 'Blue', 'Black', 'White', 'Yellow']
menu = OptionMenu(App, menu_choice, *options)
menu.pack()
menu_choice.set('white')

def show():
    msg = Label(App, text='         ', background=(menu_choice.get()).lower())
    msg.pack()

B = Button(App, text='Show', command=show)
B.pack()

App.mainloop()