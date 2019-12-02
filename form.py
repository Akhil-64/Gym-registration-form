from tkinter import *
import sqlite3

root=Tk()
root.geometry('750x750')
root.title('Gym Registration Form')
photo=PhotoImage(file="icon.gif")
root.iconphoto(False,photo)

first=StringVar()
last=StringVar()
email=StringVar()
v=StringVar()
dd=StringVar()
mm=StringVar()
yyyy=StringVar()
v2=StringVar()
v3=StringVar()
medical=StringVar()

def database():
    name1=first.get()
    name2=last.get()
    em=email.get()
    gender=v.get()
    d1=dd.get()
    d2=mm.get()
    d3=yyyy.get()
    membership=v2.get()
    condition=v3.get()
    note=medical.get()
    conn=sqlite3.connect("form.db")
    with conn:
        cursor=conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Person(First TEXT,Last TEXT,Email TEXT,Gender TEXT,DD TEXT,MM TEXT,YYYY TEXT,Membership_Duration TEXT,Medical_Condition TEXT,Additional_Medical_Note TEXT)")
    cursor.execute("INSERT INTO Person(First,Last,Email,Gender,DD,MM,YYYY,Membership_Duration,Medical_Condition,Additional_Medical_Note) values (?,?,?,?,?,?,?,?,?,?)",(name1,name2,em,gender,d1,d2,d3,membership,condition,note))
    conn.commit()
                   
                   


label_0=Label(root,text="Gym Registration Form",width=15,font="georgia 30 bold",fg="yellow",bg="black")
label_0.place(x=200,y=53)
label_0.pack(fill=BOTH)

label_01=Label(root,text="WORKOUT,EAT WELL,BE PATEINT",width=15,font="arial 20 bold",fg="blue",bg="orange")
label_01.place(x=200,y=50)
label_01.pack(fill=BOTH)


label_1=Label(root,text="First",width=20,font="arial 10")
label_1.place(x=10,y=130)

entry_1=Entry(root,bd=4,font="arial 10 italic",textvar=first,bg="powder blue")
entry_1.place(x=80,y=100)



label_10=Label(root,text="Last",width=20,font="arial 10")
label_10.place(x=170,y=130)
entry_10=Entry(root,bd=4,font="arial 10 italic",textvar=last,bg="powder blue")
entry_10.place(x=240,y=100)

label_2=Label(root,text="Email Address",width=20,font="arial 10 bold")
label_2.place(x=40,y=170)
entry_2=Entry(root,bd=4,font="arial 10 italic",width=44,textvar=email,bg="powder blue")
entry_2.place(x=77,y=200)

label_3=Label(root,text="Gender",width=20,font="arial 10 bold")
label_3.place(x=15,y=240)
v=StringVar()
Radiobutton(root,text="Male",variable=v,value="Male",activeforeground="red",width=5,relief="raised",bd=4,cursor="hand2").place(x=150,y=240)
Radiobutton(root,text="Female",variable=v,value="Female",activeforeground="red",relief="raised",bd=4,cursor="hand2").place(x=250,y=240)

label_4=Label(root,text="Membership Start Date",width=20,font="arial 10 bold")
label_4.place(x=65,y=275)
entry_2=Entry(root,width=4,bd=2,font="arial 10 italic",textvar=dd,bg="powder blue")
entry_2.place(x=75,y=300)
label_40=Label(root,text="/",width=2,font="arial 12 italic")
label_40.place(x=110,y=300)
entry_3=Entry(root,width=4,bd=2,font="arial 10 italic",textvar=mm,bg="powder blue")
entry_3.place(x=130,y=300)
label_40=Label(root,text="/",width=2,font="arial 12 italic")
label_40.place(x=160,y=300)
entry_4=Entry(root,width=7,bd=2,font="arial 10 italic",textvar=yyyy,bg="powder blue")
entry_4.place(x=180,y=300)
label_41=Label(root,text="DD",width=4,font="arial 10")
label_41.place(x=70,y=320)
label_41=Label(root,text="MM",width=4,font="arial 10")
label_41.place(x=125,y=320)
label_41=Label(root,text="YYYY",width=4,font="arial 10")
label_41.place(x=185,y=320)



label_5=Label(root,text="Membership Duration",width=20,font="arial 10 bold")
label_5.place(x=60,y=350)
v2=StringVar()
Radiobutton(root,text="1 month",variable=v2,value="1 month",activeforeground="red",cursor="hand2").place(x=70,y=380)
Radiobutton(root,text="3 months",variable=v2,value="3 months",activeforeground="red",cursor="hand2").place(x=70,y=400)
Radiobutton(root,text="6 months",variable=v2,value="6 months",activeforeground="red",cursor="hand2").place(x=70,y=420)
Radiobutton(root,text="1 year",variable=v2,value="1 year",activeforeground="red",cursor="hand2").place(x=70,y=440)
Radiobutton(root,text="Lifetime",variable=v2,value="Lifetime",activeforeground="red",cursor="hand2").place(x=70,y=460)


label_6=Label(root,text="Please indicate any pre-existing medical condition",width=50,font="arial 10 bold")
label_6.place(x=35,y=500)
list1=["Diabetes","Heart Disease","Allergies","Asthma","Fainting","High blood Pressure","Low blood Pressure","NONE"]
v3=StringVar()
droplist=OptionMenu(root,v3,*list1)
droplist.config(width=30,cursor="hand2")
v3.set("-- select condition --")
droplist.place(x=75,y=530)

label_7=Label(root,text="Additional Medical Notes :",width=30,font="arial 10 bold")
label_7.place(x=34,y=570)
paned_window=PanedWindow(height=45,width=400)
entry_5=Entry(paned_window,font="arial 10 italic",bd=4,textvar=medical,bg="powder blue")
paned_window.add(entry_5)
paned_window.place(x=75,y=600)

b1=Button(root,text="SUBMIT",width=20,bg="green",fg="white",font="arial 12 bold",cursor="hand2",command=database,bd=5).place(x=80,y=660)

root.mainloop()
