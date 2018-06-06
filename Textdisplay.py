from tkinter import *
from tkinter import font
import time
import datetime
from PIL import ImageTk,Image
import rage_sensor as rs
import light_sensor as ls
import thermistor as tr

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
        self.root.wm_attributes('-type','splash')
        self.root.configure(background='black')
        self.root.bind("<Escape>", quit)
        self.root.bind("x", quit)
        self.root.after(900, self.temp_call)
        self.root.after(1000, self.show_time)
        self.root.after(1500, self.rage_call)
        
    def show_time(self):
        tm.set(time.strftime("%H:%M:%S"))
        self.root.after(1000, self.show_time)

    def show_date(self):
        tm.set(datetime.datetime.today().strftime('%Y-%m-%d'))
        self.root.after(1000, self.show_date)

    def rage_call(self):
        ultra_val = rs.sensor()
        light_val = ls.light()
        print(ultra_val,light_val)
        if ultra_val == 1:
            self.show_meme()
        self.root.after(1000, self.rage_call)

    def temp_call(self):
        temp = round(tr.getTemp(),2)
        print(temp)
        tp.set("Room temperature: "+str(temp)+ u'\N{DEGREE SIGN}'+'C')
        self.root.after(6000, self.temp_call)
        
    def show_meme(self):
        imageFile = "getout1.png"
        im = Image.open(imageFile)
        photo = ImageTk.PhotoImage(im)
        # image = PhotoImage(file=photo)
        self.label = Label(self.root,image=photo,borderwidth=135, highlightthickness=0, bg = 'black')
        self.label.place(relx=0.5, rely=0.5, anchor = N)
        self.label.image = photo
        self.label.pack()
        self.label.after(5000,self.clear_label)

    def clear_label(self):
        print ("clear_label")
        self.label.pack_forget()

    def setweather(self):

        return

if __name__ == "__main__":

    tr.setup()

    mirror = Mirror()
    mirror.createinterface()
    fnt = font.Font(family="Courier", size=48, weight='bold', slant = 'italic')
    tm = StringVar()
    tm.set(time.strftime("%H:%M:%S"))
    dt = StringVar()
    dt.set(datetime.datetime.today().strftime('%Y-%m-%d'))
    tp = StringVar()
    tp.set("Room temperature: "+str(round(tr.getTemp(),2)) + u'\N{DEGREE SIGN}'+'C')
    
    showtime = Label(mirror.root, textvariable=tm, font= fnt, fg="white", bg="black")
    showtime.place(relx=0.01, rely=0.13, anchor=W)

    showdate = Label(mirror.root, textvariable=dt, font=fnt, fg="white", bg="black")
    showdate.place(relx=0.01, rely=0.2, anchor=W)

    title = Label(mirror.root, text="Anteater Mirror", fg = "white", bg = "black", font = fnt)
    title.place(relx=0.01, rely=0.01)
    
    temp_label = Label(mirror.root, textvariable=tp,fg = "white", bg = "black", font = fnt)
    temp_label.place(relx=0.01, rely=0.27)

    
    button=Button(mirror.root, text = "Quit", bg = 'black',highlightthickness=0, command = quit)
    button.place(relx = 0.96, rely = 0.93)

    
    

    mirror.root.mainloop()
