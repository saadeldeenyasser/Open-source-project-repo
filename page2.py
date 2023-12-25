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

def Dispage2():

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
                decode(file_path)

        elif flag2 == 2:  # -->choose LSB tech
            if flag == 1:  # --->encode +LSB
                y = ent.get()
                encode2(file_path, y)

            else:  # --->decod+LSB
                decode2(file_path)
