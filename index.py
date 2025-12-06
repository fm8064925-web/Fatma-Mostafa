from tkinter import *
root = Tk()
root.geometry("450x200")
root.title("registration form")
def getvals():
    print("accepted")
mylabel = Label(root,text="python registration form",font=("Arial",20,"bold"))
mylabel.grid(row=0,column=3)
name = Label(root,text="Name",font=("Arial",15))
phone = Label(root,text="Phone",font=("Arial",15))

gender = Label(root,text="Gender",font=("Arial",15))
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
checkvalue = IntVar
nameentry=Entry(root,textvariable=namevalue,width=50,)
phoneentry=Entry(root,textvariable=phonevalue,width=50)
genderentry=Entry(root,textvariable=gendervalue,width=50)

nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
checkbtn = Checkbutton(text="remember me?",variable=checkvalue)
checkbtn.grid(row=6,column=3)
Button (text="submit", command=getvals).grid(row=7,column=3)



root.mainloop()
        