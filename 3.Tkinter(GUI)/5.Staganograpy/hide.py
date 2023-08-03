from tkinter import *
from tkinter import filedialog
import tkinter as ttk
from PIL import Image, ImageTk
import os
import ttkbootstrap as ttk
from stegano import lsb 

root = ttk.Window(themename='morph')
root.title("Steganography")
root.geometry("700x500+150+180")
root.resizable(False, False)


def showimage():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                        title='Select Image',
                                        filetypes=(("PNG file","*.png"),
                                                  ("All file","*.txt"),
                                                  ("JPG","*.jpg")))
    
    img = Image.open(filename)
    img=ImageTk.PhotoImage(img)
    lbl.configure(image=img,width=250,height=250)
    lbl.image=img

def Hide():
    global secret
    message=text1.get(1.0,END)
    secret = lsb.hide(str(filename), message)

def Show():
    clear_message = lsb.reveal(filename)
    text1.delete(1.0, END)
    text1.insert(END, clear_message)

def save():
    secret.save("Hidden.png")



#logo
logo = PhotoImage(file = "padlock.png")
Label(root, image = logo, bg = "#2f4155").place(x = 10, y = 0)


Label(root,text="Steganography", bg = "#2d4155", fg = "white", font="ariel 25 bold").place(x=100,y=30)


#first frame
f=Frame(root,bd=3,bg="black",width=340,height=280,relief=GROOVE)
f.place(x=10,y=95)


lbl=Label(f,bg="black")
lbl.place(x=40,y=10)

#Secong Frame
f2 = Frame(root,bd=3,width=340,height=280,bg="white",relief=GROOVE)
f2.place(x=350,y=95)

text1=Text(f2,font="Robote 20",bg="white",fg="black",relief=GROOVE,wrap = WORD)
text1.place(x=0,y=0,width=320,height=295)

scrollbar1=ttk.Scrollbar(f2)
scrollbar1.place(x=320,y=0,height=300)

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# third Frame
f3 = Frame(root,bd=3,bg="#2f4155",width=330,height=90,relief=GROOVE)
f3.place(x=10,y=380)

ttk.Button(f3,text="Open Image",command=showimage).place(x=20,y=30)
ttk.Button(f3,text="Save Image",command=save,bootstyle="success").place(x=180,y=30)
ttk.Label(f3,text="Picture, Image, Photo File").place(x=20,y=5)


# fourth Frame
f4 = Frame(root,bd=3,bg="#2f4155",width=330,height=90,relief=GROOVE)
f4.place(x=360,y=380)

ttk.Button(f4,text="Hide Data",bootstyle="info",command=Hide).place(x=20,y=30)
ttk.Button(f4,text="Show Data",bootstyle="danger",command=Show).place(x=180,y=30)
ttk.Label(f4,text="Text, Message, Secret").place(x=20,y=5)




root.mainloop()