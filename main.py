from tkinter import *
from tkinter import messagebox
from gui import *

def login_main(uname,passw):
    print(uname,passw)
    if uname=="mypass" and passw=="mypass":
        messagebox.showinfo("Success","Successful Login")
        mainfunct()
        
    else:
         messagebox.showinfo("Error","Invalid Login")
         
    
def login():

  
    wndws=Tk()
    w=500;h=100
    x=(wndws.winfo_screenwidth()- w)/2
    y=(wndws.winfo_screenheight()-h)/2
    wndws.geometry("%dx%d+%d+%d" % (w,h,x,y))
    wndws.configure(bg="gold")
    wndws.title("LOGIN")
    lbl_uname=Label(wndws,text="USERNAME :").grid(row=1,column=2)
    lbl_password=Label(wndws,text="PASSOWORD :").grid(row=4,column=2)
    etry_uname=Entry(wndws)
    etry_uname.grid(row=1,column=5)
    etry_password=Entry(wndws,show="*")
    etry_password.grid(row=4,column=5)

    btn_login=Button(wndws,text="LOGIN",command=lambda:login_main(etry_uname.get(),etry_password.get()))
    btn_login.grid(row=6,column=3)

    wndws.mainloop()

login()
