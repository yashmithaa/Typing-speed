from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox 

#Install Pillow

root= Tk()
 
#Title of the page
root.title("The Title")

#icon of the page
#root.iconbitmap(r"assets/icon.ico")

frame = LabelFrame(root, text="This is the frame", padx=10, pady=10)
frame.grid(row=5,column=0,padx=100,pady=10)
b = Button(frame, text="WOW")
b.pack()

#Adding Image
'''myImage = ImageTk.PhotoImage(Image.open("assets/pink.png"))
myLabel1 = Label(image=myImage)
myLabel1.grid(row=6, column=0)'''

#Button Action
def myClick():
    myLabel2 = Label(root, text="Hello " + myinput.get()).grid(row=3,column=0)

#Replacing Text box value
def button_click(number):
    myinput.delete(0, END)
    myinput.insert(0, number)

#Label Widget
myLabel = Label(root, text="Enter your name").grid(row=0, column=0)

#Input Wdiget
myinput = Entry(root, width=50, bg="white", fg ="black", borderwidth="5") #,show='*')
myinput.grid(row=0, column=1)
myinput.insert(0, "Enter your Name: ")

#Button Widget
mybutton = Button(root, text='Done', padx=70, pady=10, command=myClick, fg="#000000", bg="white").grid(row=1, column=0, columnspan=2)

#Button with a value
mybutton1 = Button(root, text='12', padx=70, pady=10, command=lambda: button_click(12))
mybutton1.grid(row=0, column=4)

#Exit Button
exitbutton = Button(root, text='Exit Program', command=root.quit)
exitbutton.grid(row=4, column=0, columnspan=3)

#Anchored Label
myLabel2 = Label(root, text="Enter your name", bd=1, relief=SUNKEN, anchor=E)
myLabel2.grid(row=3,column=0, columnspan=3, sticky=W+E)

#Radio Button

r=IntVar()
r.set("2")

def clicked(value):
    myLabel3=Label(root,text=value)
    myLabel3.grid(row=5,column=3)

Radiobutton(root, text="Option 1", variable=r, value=1).grid(row=2,column=3)
Radiobutton(root, text="Option 2", variable=r, value=2).grid(row=3,column=3)


myButton2 = Button(root, text="click me",command=lambda: clicked(r.get()))
myButton2.grid(row=4, column=3)

#Message box

def popup():
    response=messagebox.askyesno("WARNING", "Click the correct option")
    if response==1:
        messagebox.showwarning("WARNING", "You are dumb")
    elif response==0:
        messagebox.showwarning("WARNING", "You are dumb")

myButton4=Button(root, text="Don't click", command=popup)
myButton4.grid(row=3, column=4)

# to disable button: state=DISABLED
# to take value of button:  command=Lambda: button_click(12)
# to remove something from the menu:  grid_forget()

#opening a new window
def open():
    top = Toplevel()

    top.title("Login")
    top.iconbitmap(r"assets/icon.ico")
    top.geometry("1920x1080")

    #adding image as background
    global img
    img = PhotoImage(file=r"pink.png")
    label = Label(top,image=img)
    label.place(x=0, y=0)

btn = Button(root, text="Login", command=open)
btn.grid(row=4,column=0)


root.mainloop() 
