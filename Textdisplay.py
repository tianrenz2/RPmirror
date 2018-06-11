from tkinter import *
from tkinter import font
import time
import datetime
from PIL import ImageTk,Image
import rage_sensor as rs
import light_sensor as ls
import thermistor as tr
import sendemail
import voice
import threading
import speech_recognition as sr


class Mirror:
    label = None
    root = None
    tm,dt,tp = None,None,None
    fnt = None
    showtime,showdate = None,None
    temp_label = None
    title = None
    pre = 1
    mode = 0

    voicetext = ""
    
    def __init__(self):
        self.root = Tk()
        self.label = Label(self.root)
        self.tm = StringVar()
        self.dt = StringVar()
        self.tp = StringVar()

        self.fnt = font.Font(family="Times New Roman", size=48, weight='bold', slant = 'italic')
        self.title = Label(self.root, text="Anteater Mirror", fg = "white", bg = "black", font = self.fnt)
        self.title.place(relx=0.01, rely=0.01)
        self.root.after(1000, self.thr)

        
    def switch(self):
        print("mode",self.mode)
        if self.mode == 0:
            self.safemode()
        else:
            self.actmode()
            
    def quit(self,*args):
        self.root.destroy()
    
    def safemode(self):
        self.tm.set('')
        self.dt.set('')
        self.tp.set('')
        self.mode = 1
        self.root.after(100, self.rage_call)

    def actmode(self):
        self.mode = 0
        print("active mode! %d",self.mode)
        self.temp_init()
        
        self.tm.set(time.strftime("%H:%M:%S"))
        self.dt.set(datetime.datetime.today().strftime('%Y-%m-%d'))
        
        self.showtime = Label(mirror.root, textvariable=self.tm, font= self.fnt, fg="white", bg="black")
        self.showtime.place(relx=0.01, rely=0.13, anchor=W)
        self.showdate = Label(mirror.root, textvariable=self.dt, font= self.fnt, fg="white", bg="black")
        self.showdate.place(relx=0.01, rely=0.2, anchor=W)
        self.root.after(1000, self.show_time)
        self.root.after(1000, self.show_date)
        
    def createinterface(self):
        self.root.attributes("-fullscreen", False)
        self.root.geometry("{0}x{1}+0+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        self.root.wm_attributes('-type','splash')
        self.root.configure(background='black')
        self.root.bind("<Escape>", quit)
        self.root.bind("x", quit)
        self.actmode()
        
    def show_time(self):
        if self.mode == 0:
            self.tm.set(time.strftime("%H:%M:%S"))
            self.root.after(1000, self.show_time)

    def show_date(self):
        if self.mode == 0:
            self.dt.set(datetime.datetime.today().strftime('%Y-%m-%d'))
            self.root.after(1000, self.show_date)

    def rage_call(self):
        ultra_val = rs.sensor()
        light_val = ls.light()
        if self.mode == 1:
            print(ultra_val,light_val)
            if ultra_val == 1 or light_val != self.pre:
                self.pre = light_val
                self.show_meme()
                sendemail.sendemail()
                self.root.after(3000, self.rage_call)
            else:
                self.pre = light_val
                self.root.after(1000, self.rage_call)
            
            
    def temp_init(self):
        if self.mode == 0:
            temp = round(tr.getTemp(),2)
            self.tp.set("Room temperature: "+str(temp)+ u'\N{DEGREE SIGN}'+'C')
            self.temp_label = Label(mirror.root, textvariable=self.tp,fg = "white", bg = "black", font = self.fnt)
            self.temp_label.place(relx=0.01, rely=0.27)
            self.temp_call()
    
    def temp_call(self):
        if self.mode == 0:
            temp = round(tr.getTemp(),2)
            self.tp.set("Room temperature: "+str(temp)+ u'\N{DEGREE SIGN}'+'C')
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
        self.label.after(3000,self.clear_label,self.label)

    def clear_label(self,label):
        print ("clear_label")
        label.pack_forget()

    def update_recognized_text(self):
        print(recognizer.recognized_text)
        self.root.after(100, self.update_recognized_text)

        
    def thr(self):
        t1 = threading.Thread(target=self.listen, daemon=True)
        t1.start()

    def listen(self):
        r = sr.Recognizer()
        while True:
            with sr.Microphone() as source:
                audio = r.listen(source)
                try:
                    text = r.recognize_google(audio)
                    print(text)
##                    if text == "switch" or text == 'such' or text == "switch switch":
                    if text == 'security' or text == 'pineapple':
                        self.switch()
                except Exception as e:
                    print(e)

    
class SpeechRecognizer(threading.Thread):
     recognized_text = ''
     def __init__(self):
         super(SpeechRecognizer, self).__init__()
         self.setDaemon(True)
         self.recognized_text = ""

     def run(self):
        self.recognized_text = voice.listen()


 

if __name__ == "__main__":

    tr.setup()

    mirror = Mirror()
    mirror.createinterface()
    
    
    button=Button(mirror.root, text = "Quit", bg = 'black',highlightthickness=0, command = mirror.quit)
    button.place(relx = 0.96, rely = 0.93)

    
    

    mirror.root.mainloop()
