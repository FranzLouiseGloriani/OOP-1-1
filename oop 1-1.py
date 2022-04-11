from tkinter import *
window = Tk()

window.geometry("500x600+30+20")
window.title("Welcome to Python Programming")

#add Button widget
btn = Button(window, text="Click to add name", fg="blue")
btn.place(x=80, y=100)

#Add label widget
lbl = Label(window, text="Student Personal Information", fg="Blue", bg="Orange")
lbl.place(relx=.5, y=50, anchor="center")
lbl2 = Label(window, text="Gender", fg="purple")
lbl2.place(x=80, y=150)
lbl3 = Label(window, text="Sports", fg="purple")
lbl3.place(x=80, y=250)
lbl4 = Label(window, text="Subjects", fg="purple")
lbl4.place(x=80, y=350)

#Add text field widget
txtfld = Entry(window, bd=3, font=("verdana", 16))
txtfld.place(x=150, y=100)

#Add radio button widget
v1 = StringVar()
v2 = StringVar()
v1.set(str(1))
r1 = Radiobutton(window, text="Male", value=1)
r1.place(x=80, y=200)
r2 = Radiobutton(window, text="Female", value=2)
r2.place(x=140, y=200)

#Add check button widget
v3 = IntVar()
v4 = IntVar()
v5 = IntVar()
chkbox = Checkbutton(window, text="Basketball", variable=v3)
chkbox2 = Checkbutton(window, text="Tennis", variable=v4)
chkbox3 = Checkbutton(window, text="Swimming", variable=v5)
chkbox.place(x=80, y=300)
chkbox2.place(x=160, y=300)
chkbox3.place(x=220, y=300)

#Add list box widget
data = "Student1", "Student2", "Student3"
var = StringVar()
var.set("Student1")
data1 = "Arithmetic"
data2 = "Reading"
data3 = "Writing"
listbox = Listbox(window, height=3, selectmode="single")
listbox.insert(END, data1, data2, data3)
listbox.place(x=80, y=400)

window.mainloop()
