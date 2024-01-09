# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk

root=Tk()

#setting the geometry of the BMI Calculator
root.title("BMI Calculator")
root.geometry("470x580+300+200")
root.resizable(False,False)
root.configure(bg="#f0f1f5")

def BMI():
    ht = float(h.get())
    wt = float(w.get())
    m=ht/100
    bmi=round(float(wt/m**2),1)
    label1.config(text=bmi)

    #checking conditions of health
    if bmi<=18.5:
        label2.config(text="Underweight!")
        label3.config(text="Your body weight is hence lower than normal!")
    elif bmi>18.5 and bmi<=25:
        label2.config(text="Normal.")
        label3.config(text="Congratulations your body weight is normal!")
    elif bmi>25 and bmi<=30:
        label2.config(text="Overweight!")
        label3.config(text="Your body weight is slightly above normal!!")
    else:
        label2.config(text="Obes!")
        label3.config(text="Your health is at risk.You should visit a doctor!")

#icon
image_icon=PhotoImage(file="icon.png")
root.iconphoto(True,image_icon)

#top picture
top=PhotoImage(file="top.png")
top_label=Label(root,image=top,background="#f0f1f5")
top_label.place(x=-10,y=-10)

#bottom picture
bottom_label=Label(root,width=72,height=18,bg="lightblue")
bottom_label.pack(side=BOTTOM)

#boxes
box=PhotoImage(file="box.png")
Label(root,image=box).place(x=20,y=100)
Label(root,image=box).place(x=240,y=100)

#scale
scale=PhotoImage(file="scale.png")
scale_label=Label(root,image=scale,bg="lightblue")
scale_label.place(x=20,y=310)

#slider1
current_val=tk.DoubleVar()
def get_current_val():
    return '{: .2f}'.format(current_val.get())
def slider_changed(event):
    h.set(get_current_val())
    size=int(float(get_current_val()))
    img=(Image.open("man.png"))
    resized_img=img.resize((50,10+size))
    photo2=ImageTk.PhotoImage(resized_img)
    man_label.config(image=photo2)
    man_label.place(x=70,y=550-size)
    man_label.image=photo2

style=ttk.Style()
style.configure("TScale",background="white")
slider=ttk.Scale(root,from_=0 ,to=220,orient="horizontal",style="TScale",command=slider_changed,variable=current_val)
slider.place(x=80,y=250)

#slider2
current_val2=tk.DoubleVar()
def get_current_val2():
    return '{: .2f}'.format(current_val2.get())
def slider_changed2(event):
    w.set(get_current_val2())
style2=ttk.Style()
style2.configure("TScale",background="white")
slider2=ttk.Scale(root,from_=0 ,to=200,orient="horizontal",style="TScale",command=slider_changed2,variable=current_val2)
slider2.place(x=300,y=250)

#entry box
h=StringVar()
w=StringVar()
height=Entry(root,textvariable=h,width=5,font='arial 50',bg="#fff",fg="#000",bd=0,justify=CENTER)
height.place(x=35,y=160)
h.set(get_current_val())
weight=Entry(root,textvariable=w,width=5,font='arial 50',bg="#fff",fg="#000",bd=0,justify=CENTER)
weight.place(x=255,y=160)
w.set(get_current_val2())

#image of man
man_label=Label(root,bg="lightblue")
man_label.place(x=70,y=400)

#button for view report
Button(root,text="View Report",width=15,height=2,font="arial 10 bold",bg="#1f6e68",fg="white",command=BMI).place(x=280,y=340)

#bmi report writing
label1=Label(root,font="arial 50 bold",bg="lightblue",fg="#fff")
label1.place(x=125,y=305)
label2=Label(root,font="arial 30 bold",bg="lightblue",fg="#3b3a3a")
label2.place(x=200,y=430)
label3=Label(root,font="arial 11 bold",bg="lightblue",fg="#fff")
label3.place(x=136,y=500)


root.mainloop()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
