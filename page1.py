from tkinter import *
from append import encode, decode
from tkinter import filedialog
from tkinter import ttk
from lsb import encode2, decode2
# root.iconify()  # Hide the root window

def action():
    pro.destroy()
    from tist import page1
    page1()

def Dispage1():

    def browse_file():
        global file_path
        file_path = filedialog.askopenfilename()

    def choosetec2():
        global flag2
        flag2 = 2

    def choosetec1():
        global flag2
        flag2 = 1

    def choose1():

        global flag
        flag = 1

    def choose2():

        global flag
        flag = 2

    def getpath():
        if flag2 == 1:  # -->choose Append technique
            if flag == 1:  # --->encode +append
                global y
                y = ent.get()
                encode(file_path, y)  # --->decode + append

            else:

                ent.delete(0, END)
                ent.insert(0, decode(file_path))
        elif flag2 == 2:  # -->choose LSB tech
            if flag == 1:  # --->encode +LSB
                y = ent.get()
                encode2(file_path, y)

            else:  # --->decod+LSB
                ent.delete(0, END)
                ent.insert(0,decode2(file_path))

    global pro
    pro = Tk()
    pro.title('Security Tool')
    pro.geometry("700x500+350+90")
    pro.resizable(False, False)
    pro.config(background='#3E3646')
    pro.iconbitmap('hider.ico')
    style = ttk.Style()
    style.configure("TRadiobutton", background="#A6A4A7")

    But1 = Button(pro, text="Home", foreground='white', background="#A6A4A7", font=20, command=action)
    But1.place(x=10, y=10, width=150, height=30)

    But2 = Button(pro, text="About", foreground='white', background="#A6A4A7", font=20)
    But2.place(x=170, y=10, width=150, height=30)

    lb1 = Label(pro, text="Img steganography ", foreground='white', bg="#3E3646", font=("Arial", 30, "bold"))
    lb1.place(x=165, y=80)

    lb2 = Label(pro, text="enter secret message :", foreground='white', bg="#3E3646", font=30)
    lb2.place(x=20, y=150)

    ent = Entry(pro, foreground='black', bg="#A6A4A7")
    ent.place(x=250, y=155, width=180, height=25)



    lb3 = Label(pro, text="choose image file :", foreground='white', bg="#3E3646", font=30)
    lb3.place(x=20, y=195)

    But3 = Button(pro, text="Browse", command=browse_file, foreground='white', bg="#A6A4A7")
    But3.place(x=250, y=200, width=180, height=25)

    lb4 = Label(pro, text="choose option :", foreground='white', bg="#3E3646", font=30)
    lb4.place(x=22, y=250)

    var1 = IntVar()
    var2 = StringVar()
    rad = ttk.Radiobutton(pro, text="Encode", value=1, command=choose1, variable=var1)
    rad.place(x=200, y=255)

    rad2 = ttk.Radiobutton(pro, text="decode", value=2, command=choose2, variable=var1)
    rad2.place(x=415, y=255, )

    lb5 = Label(pro, text="choose technique :", foreground='white', bg="#3E3646", font=30)
    lb5.place(x=22, y=290)

    rad3 = ttk.Radiobutton(pro, text="Append", value="a", command=choosetec1, variable=var2)
    rad3.place(x=200, y=295)

    rad4 = ttk.Radiobutton(pro, text="LSB(more secure)", value="b", command=choosetec2, variable=var2)
    rad4.place(x=415, y=295, )

    But4 = Button(pro, text="Apply", foreground="white", background="#A6A4A7", font=20, command=getpath)
    But4.place(x=250, y=350, width=180, height=50)





# def gotopage1():
#     page2.destroy()  # Close the page2 window
#     root.deiconify()  # Show the root window