import sys
import os
import bot
import speech_recognition as sr
from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.geometry('500x500')
root.title("Home")


# bg = PhotoImage(file = r"C:\Users\ASUS\Downloads\loginbg.gif") 
  
# Create Canvas 
canvas1 = Canvas( root, width = 400, 
                 height = 400) 
  
canvas1.pack(fill = "both", expand = True) 
  
# Display image 
#canvas1.create_image( 0, 0, image = bg, anchor = "nw") 

username = Label(root,text = "Email  : \n or \n Phone No ")
username.place(x = 100, y = 100)

user_txt = Entry(root)
user_txt.place(x = 200, y = 100)

pwd = Label(root,text = "Password : ")
pwd.place(x = 100, y = 200)

pwd_txt = Entry(root, show = "*")
pwd_txt.place(x = 200, y = 200)

photo = PhotoImage(file = r"C:\Users\ASUS\Downloads\mike2.gif") 

def start(name):
    f = open('auth.txt','w')
    f.write(user_txt.get()+'\n')
    f.write(pwd_txt.get()+'\n')
    f.write(name.get())
    f.close()
    bot.run()
    # os.system('python bot.py')

def listen(name):
    print("Listening...")
    r = sr.Recognizer()
    with sr.Microphone() as source:               # use the default microphone as the audio source
        audio = r.listen(source)   
    try:
        prod = r.recognize_google(audio)
        print(prod+"\n")                          # recognize speech using Google Speech Recognition
        name.insert(0,prod)
        start(name)
    except LookupError:                           # speech is unintelligible
        print("Please try again!")
    

def click():
    top = Toplevel()
    top.geometry("400x400")
    top.title("Product Info")
    lbl = Label(top, text = "Product ").place(x = 180, y = 100)
    name = Entry(top)
    name.place(x = 150, y = 150)
    mike=Button(top, text = 'Click Me !',command=lambda:listen(name), image = photo,width=30,height=38).place(x = 300, y = 130) 
    go = Button(top, text = " Go !   ", command = lambda: start(name)).place(x = 180, y = 200)


    
button = Button(root, text = "Next >>",command=click).place(x = 200, y = 300)

root.mainloop()