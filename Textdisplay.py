from tkinter import *
from tkinter import font
import time
import datetime
from PIL import ImageTk,Image
import os



class Mirror:
    label = None
    root = None
    def __init__(self):
        self.root = Tk()
        self.label = Label(self.root)
    def quit(self,*args):
        self.root.destroy()

    def createinterface(self):
        self.root.attributes("-fullscreen", False)
        self.root.geometry("{0}x{1}+0+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight()))

        self.root.configure(background='black')
        self.root.bind("<Escape>", quit)
        self.root.bind("x", quit)
        self.root.after(1000, self.show_time)

    def show_time(self):
        tm.set(time.strftime("%H:%M:%S"))
        self.root.after(1000, self.show_time)

    def show_date(self):
        tm.set(datetime.datetime.today().strftime('%Y-%m-%d'))
        self.root.after(1000, self.show_date)

    def show_meme(self):
        imageFile = "getout1.png"
        im = Image.open(imageFile)
        photo = ImageTk.PhotoImage(im)
        # image = PhotoImage(file=photo)
        self.label = Label(self.root,image=photo,borderwidth=135, highlightthickness=0, bg = 'black')
        self.label.place(relx=0.5, rely=0.5, anchor = N)
        self.label.image = photo
        self.label.pack()
        self.label.after(6000,self.clear_label)

    def clear_label(self):
        print ("clear_label")
        self.label.pack_forget()

    def setweather(self):
        return



if __name__ == "__main__":

    mirror = Mirror()
    mirror.createinterface()
    fnt = font.Font(family='Apple Chancery', size=38, weight='bold')
    tm = StringVar()
    tm.set(time.strftime("%H:%M:%S"))
    dt = StringVar()
    dt.set(datetime.datetime.today().strftime('%Y-%m-%d'))

    showtime = Label(mirror.root, textvariable=tm, font=fnt, fg="white", bg="black")
    showtime.place(relx=0.01, rely=0.13, anchor=W)

    showdate = Label(mirror.root, textvariable=dt, font=fnt, fg="white", bg="black")
    showdate.place(relx=0.11, rely=0.13, anchor=W)

    title = Label(mirror.root, text="Anteater Mirror",fg = "white", bg = "black", font = fnt)
    title.place(relx=0.01, rely=0.01)

    mirror.show_meme()


    mirror.root.mainloop()