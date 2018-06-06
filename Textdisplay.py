from tkinter import *
from tkinter import font
import time
import datetime
from PIL import ImageTk,Image
import os


root = Tk()

def quit(*args):
    root.destroy()


def createinterface():
    root.attributes("-fullscreen", False)
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

    root.configure(background='black')
    root.bind("<Escape>", quit)
    root.bind("x", quit)
    root.after(1000, show_time)

def show_time():
    tm.set(time.strftime("%H:%M:%S"))
    root.after(1000, show_time)

def show_date():
    tm.set(datetime.datetime.today().strftime('%Y-%m-%d'))
    root.after(1000, show_date)

def show_meme():
    imageFile = "getout1.png"
    im = Image.open(imageFile)
    photo = ImageTk.PhotoImage(im)
    # image = PhotoImage(file=photo)
    label = Label(root,image=photo,borderwidth=135, highlightthickness=0, bg = 'black')
    label.place(relx=0.5, rely=0.5, anchor = N)
    label.image = photo
    label.pack()

def setweather():
    return



if __name__ == "__main__":
    createinterface()
    fnt = font.Font(family='Apple Chancery', size=38, weight='bold')
    tm = StringVar()
    tm.set(time.strftime("%H:%M:%S"))
    dt = StringVar()
    dt.set(datetime.datetime.today().strftime('%Y-%m-%d'))

    showtime = Label(root, textvariable=tm, font=fnt, fg="white", bg="black")
    showtime.place(relx=0.01, rely=0.13, anchor=W)

    showdate = Label(root, textvariable=dt, font=fnt, fg="white", bg="black")
    showdate.place(relx=0.11, rely=0.13, anchor=W)

    title = Label(root, text="Anteater Mirror",fg = "white", bg = "black", font = fnt)
    title.place(relx=0.01, rely=0.01)

    show_meme()


    root.mainloop()