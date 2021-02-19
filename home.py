import sys
import os
import bot
import speech_recognition as sr
import random
import string
import re
from tkinter import *
from PIL import ImageTk,Image
from captcha.image import ImageCaptcha

def createImage(flag=0):
    """
    Defining the method createImage() which will create
    and generate a Captcha Image based on a randomly
    generated strings. The Captcha Image generated is then
    incorporated into the GUI window we have designed.
    """
    global random_string
    global image_label
    global image_display
    global entry
    global verify_label
    # The if block below works only when we press the
    # Reload Button in the GUI. It basically removes
    # the label (if visible) which shows whether the
    # entered string is correct or incorrect.
    if flag == 1:
        verify_label.grid_forget()
    # Removing the contents of the input box.
    entry.delete(0, END)
    # Generating a random string for the Captcha
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    # Creating a Captcha Image
    image_captcha = ImageCaptcha(width=150, height=75)
    image_generated = image_captcha.generate(random_string)
    image_display = ImageTk.PhotoImage(Image.open(image_generated))
    # Removing the previous Image (if present) and
    # displaying a new one.
    image_label.grid_forget()
    image_label = Label(root, image=image_display)
    image_label.place(x=490, y=270)
def check(x, y):
    """
    Defining the method check() which will check
    whether the string entered by the user matches
    with the randomly generated string. If there is
    a match then "Verified" pops up in the window.
    Otherwise, "Incorrect!" pops up and a new Captcha
    Image is generated for the user to try again.
    """
    # Making the scope of the below mentioned
    # variables because their values are accessed
    # globally in this script.
    global verify_label
    verify_label.grid_forget()
    if x.lower() == y.lower():
        verify_label = Label(master=root,
                             text="Verified!",
                             font="Arial 15",
                             bg='#D3D3D3',
                             fg="#00a806"
                             )
        verify_label.place(x=420, y=370)
    else:
        verify_label = Label(master=root,
                             text="Retry!",
                             font="Arial 15",
                             bg='#D3D3D3',
                             fg="#fa0800"
                             )
        verify_label.place(x=420, y=370)
        createImage()

root = Tk()
root.geometry('1150x650')
root.title("Home")
BG=PhotoImage(file=r"C:\Users\ASUS\Downloads\bg7.png")
C=Canvas(root,width=1150,height=650)
C.pack(fill="both",expand=True)
C.create_image(0,0,image=BG)



username = Label(root,text = "Email or Phone No : ")
username.place(x = 350, y = 100)

user_txt = Entry(root)
user_txt.place(x = 500, y = 100,height=25)

pwd = Label(root,text = "Password : ")
pwd.place(x = 400, y = 200)

pwd_txt = Entry(root, show = "*")
pwd_txt.place(x = 500, y = 200,height=25)

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
    
reg='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
def chk1(email):
    if(re.search(reg,email) is None):
        return False
    else:
        return True
reg1='^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*$'
def chk2(phone):
    if(re.search(reg1,phone) is None):
        return False
    else:
        return True

v1 = IntVar()
def show1():   
    print(str(v1.get()))

def click():
    if(chk1("cheraujain@gmail.com")==False and chk2("9876543210")==False):
        print("Invalid")
    else:
        print("Valid")
    top = Toplevel()
    top.geometry("700x650")
    top.title("Product Info")

    global BG1
    BG1=PhotoImage(file=r"C:\Users\ASUS\Downloads\2b71ca7b90810dd16981b83702ec67fc.png")
    C1=Canvas(top,width=700,height=650)
    C1.pack(fill="both",expand=True)
    C1.create_image(0,0,image=BG1)

    lbl = Label(top, text = "Product ").place(x = 315, y = 200)
    name = Entry(top)
    name.place(x = 270, y = 300)
    mike=Button(top, text = 'Click Me !',command=lambda:listen(name), image = photo,width=30,height=38).place(x = 430, y = 280) 
    s1 = Scale( top, variable = v1,  
               from_ = 1000, to = 55000,  
               orient = HORIZONTAL,length=200).place(x=240,y=380)    
    l3 = Label(top, text = "Max. Price") 

    b1 = Button(top, text ="Choose",  
                command = show1,  
                bg = "lightyellow")   
    b2 = Button(top, text ="Max. Price",  
            command = show1,  
            bg = "lightyellow").place(x=320,y=450)   


    go = Button(top, text = " Go !   ", command = lambda: start(name)).place(x = 328, y = 530)


# Initializing the Variables to be defined later
verify_label = Label(root)
image_label = Label(root)
    # Defining the Input Box and placing it in the window
entry = Entry(root, width=11,
                  font="Arial 15", justify="center")
entry.place(x=500, y=370)
    # Creating an Image for the first time.
createImage()
    # Defining the path for the reload button image
    # and using it to add the reload button in theB
    # GUI window
path = r"C:\\Users\\ASUS\\Downloads\\refresh+reload+update+icon-1320191166843452904.png"
reload_img = ImageTk.PhotoImage(Image.open(path).resize((32, 32), Image.ANTIALIAS))
reload_button = Button(image=reload_img, command=lambda: createImage(1))
reload_button.place(x=650, y=365)
    # Defining the submit button
submit_button = Button(root, text="Verify", font="Arial 10", command=lambda: check(entry.get(), random_string))
submit_button.place(x=550, y=435)
root.bind('<Return>', func=lambda Event: check(entry.get(), random_string))
   
button = Button(root, text = "Next >>",command=click).place(x = 1000, y = 550)

root.mainloop()
