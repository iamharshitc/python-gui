

from tkinter import *
from pymysql import  *
obj = Tk()
obj.geometry('500x500')
obj.title("Registration Form")
obj.configure(bg="#8B8BDF")

def sample():
    # print("in index")
    con = connect(db="batch530", user="root", password="root", host="localhost")
    cur = con.cursor()
    id = int(e1.get())
    name = e2.get()
    age = int(e3.get())
    cur.execute("insert into register values (%d,'%s',%d)"%(id,name,age))
    con.commit()
    print("inserted")
    con.close()
def example():
    obj.destroy()
    root=Tk()
    root.mainloop()
l1 = Label(obj,text="Registration Form",font=('bold',25),bg="#8B8BDF",fg='white')

l2 = Label(obj,text="Enter ID",font=('bold',15),bg="#8B8BDF",fg='white')
l3 = Label(obj,text="Enter Name",font=('bold',15),bg="#8B8BDF",fg='white')
l4 = Label(obj,text="Enter Age",font=('bold',15),bg="#8B8BDF",fg='white')

e1 = Entry(obj,width=20,font=('bold',20))
e2 = Entry(obj,width=20,font=('bold',20))
e3 = Entry(obj,width=20,font=('bold',20))

b1 = Button(obj,text = "Enter",padx=20,pady=10,font=('bold',20),command=sample)
b2 = Button(obj,text = "Exit",padx=20,pady=10,font=('bold',20),command=example)

l1.pack()
l2.pack()
e1.pack(ipadx=10,ipady=10)
l3.pack()
e2.pack(ipadx=10,ipady=10)
l4.pack()
e3.pack(ipadx=10,ipady=10)

b1.pack()
b2.pack()

obj.mainloop()

