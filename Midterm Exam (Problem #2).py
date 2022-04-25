from tkinter import *
window = Tk()

def fullname():
    full_name = txtfld.get()
    txtfld2.insert(END, full_name)

window.geometry("540x270")
window.title("Midterm in OOP")

lbl = Label(window, text="Enter your fullname:", fg="Red", font=("arial", 8))
lbl.place(x=45, y=85)

txtfld = Entry(window, bd=5, font=13)
txtfld.place(x=270, y=85)
txtfld2 = Entry(window, bd=5, font=13)
txtfld2.place(x=270, y=130)

btn = Button(window, text="Click to display your Fullname", fg="Red", font=("arial", 8), command=fullname)
btn.place(x=45, y=130)

window.mainloop()
