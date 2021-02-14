from tkinter import *
from pytube import *
from tkinter import messagebox 
import os
try:
    os.mkdir("yt video")
    os.mkdir("yt audio")
except:
    eroor=2
def search():
    try:
        why=var.get()
        url=yrl.get()
        yt=YouTube(url)
        yt_video=yt.streams.filter(progressive=True).first()
        yt_audio=yt.streams.filter(only_audio=True).first()
        # thumb=yt.thumbnail_url
        til=yt.title
    except:
        messagebox.showerror("error", "you have error check URL or contect me on insta => aashish_vishnu_yash")
        
    if(why == 1):
        try:
            yt_video.download("yt video")
        except:
            messagebox.showerror("error", "delete your old file  or contect me on insta => aashish_vishnu_yash")
        messagebox.showinfo("showinfo", f"{til}have successfully downloaded")
    elif(why == 2):
        try:
            yt_audio.download("yt audio")
        except:
            messagebox.showerror("error", "delete your old file  or contect me on insta => aashish_vishnu_yash")
        messagebox.showinfo("showinfo", f"{til}have successfully downloaded")
    else:
        messagebox.showerror("error", "select formet or contect me on insta => aashish_vishnu_yash")
    

root =Tk()
yrl=StringVar()
var=IntVar()

root.geometry("500x250+300+50")
root.configure(bg='blue')
title=Label(root,text="YT DOWNLOADER BY VISHNU-YASH",font=("times new roman",15),bg='black',fg='white').pack(side="top",fill=X)
t1=Label(root,text="URL",font=("times new roman",15),bg='blue',fg='white').place(x=10,y=50)
e1= Entry(root,font=("times new roman",13),textvariable=yrl).place(x=120,y=50,width=340)
R1 = Radiobutton(root, text="video formet", variable=var, value=1,bg='blue',fg='red',font=("times new roman",15)).place(x=10,y=75)
R2 = Radiobutton(root, text="audio formet", variable=var, value=2,bg='blue',fg='red',font=("times new roman",15)).place(x=150,y=75 )
b5=Button(root,text="search",command=search)
b5.place(x=350,y=90,height=30,width=120)


root.mainloop()
