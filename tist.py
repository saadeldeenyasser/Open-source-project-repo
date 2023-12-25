from tkinter import *
def action1():
    root.destroy()  # Hide the root window
    import page1
    page1.Dispage1()

def action2():
    root.destroy()
    import page2
    page2.Dispage2()
def action3():
    root.destroy()
    import page3
    page3.Dispage3()
def action4():
    root.destroy()
    import page4
    page4.Dispage4()
def page1():
    global root
    root = Tk()
    root.title('Security Tool')
    root.geometry("700x500+350+90")
    root.resizable(False, False)
    root.config(background='#3E3646')
    root.resizable(False, False)
    root.iconbitmap('hider.ico')


    But1 = Button(root, text="Image", foreground='white', background="#A6A4A7", font=20, command=action1)
    But1.place(x=120, y=140, width=170, height=60)

    But2 = Button(root, text="Video", foreground='white', background="#A6A4A7", font=20, command=action2)
    But2.place(x=420, y=140, width=170, height=60)

    But3 = Button(root, text="Audio", foreground='white', background="#A6A4A7", font=20, command=action3)
    But3.place(x=120, y=240, width=170, height=60)

    But4 = Button(root, text="Text", foreground='white', background="#A6A4A7", font=20, command=action4)
    But4.place(x=420, y=240, width=170, height=60)

    root.mainloop()

if __name__ == "__main__":
    page1()
