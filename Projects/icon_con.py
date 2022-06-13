from re import L
from tkinter import *

App = Tk()
App.title("Icon Converter")
App.geometry("400x200")

def open_img():
    from PIL import Image
    from tkinter import filedialog
    global img
    
    App.img_dir = filedialog.askopenfilename(initialdir="/", title="Select an image", filetypes=(("png files", "*.png"), ("all files", "*.*")))
    img = Image.open(App.img_dir)


def conv_img():
    from PIL import Image
    
    img.save(f'{ico_name.get()}.ico', format='ICO', sizes=[(ico_size.get(), ico_size.get())])
    
    success = Toplevel()
    success.title("Success")
    
    msg = Label(success, text="Successfully converted!")
    msg.pack()    
    
    success.mainloop()


def preview():
    prev = Toplevel()
    prev.title("Preview")
    prev.iconbitmap(f'{ico_name.get()}.ico')
    
    prev_lbl = Label(prev, text="Check out your icon!")
    prev_lbl.pack()
    
    prev.mainloop()


chooseL = Label(App, text="Choose an image: ")
chooseL.grid(row=0, column=0, sticky=W)

chooseB = Button(App, text="Choose", command=open_img)
chooseB.grid(row=0, column=1, sticky=W)

sizeL = Label(App, text="Select a size for the icon: ")
sizeL.grid(row=1, column=0, sticky=W)

ico_size = IntVar()
sizes_options = [16,24,32,48,64,96,128,255]
ico_size.set(32)
size_menu = OptionMenu(App, ico_size, *sizes_options)
size_menu.grid(row=1, column=1, sticky=W)

fnameL = Label(App, text="Choose a name for the icon: ")
fnameL.grid(row=2, column=0, sticky=W)

ico_name = Entry(App)
ico_name.grid(row=2, column=1, sticky=W)

convB = Button(App, text="Convert", command=conv_img)
convB.grid(row=3, column=0, sticky=W)

prevB = Button(App, text="Preview", command=preview)
prevB.grid(row=3, column=1, sticky=W)

App.mainloop()
