from tkinter import *
from tkinter import messagebox

def save_details():
    if messagebox.askyesno("Save Details","Are you Sure"):
        book_name=a1.get()
        book_author=b1.get()
        book_edition=c1.get()
        book_price=d1.get()

        with open("Book_detail.txt","a") as file:
            file.write(book_name)
            file.write(book_author)
            file.write(book_edition)
            file.write(book_price)

        messagebox.showinfo("Saved","Details saved successfully")    

def clear_details():
    a1.delete(0,END)
    b1.delete(0,END)
    c1.delete(0,END)
    d1.delete(0,END)


f=Tk()
f.geometry("800x800")
f.title("Library")

p=Label(f,text="Library",font="bold")
p.place(x=350,y=100)

a=Label(f,text="Book Name")
a.place(x=30,y=200)
a1=Entry(f)
a1.place(x=200,y=200)

b=Label(f,text="Book Author")
b.place(x=30,y=250)
b1=Entry(f)
b1.place(x=200,y=250)


c=Label(f,text="Book Edition")
c.place(x=30,y=300)
c1=Entry(f)
c1.place(x=200,y=300)

d=Label(f,text="Book Price")
d.place(x=30,y=350)
d1=Entry(f)
d1.place(x=200,y=350)

e= Button(f, text="Save Details", font="arialblack",command=save_details)
e.place(x=250, y=400)

g= Button(f, text="Clear", font="arialblack",command=clear_details)
g.place(x=450, y=400)


f.mainloop()




