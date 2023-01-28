from tkinter import *

root = Tk()

def click(event):
    global txt_on_screen
    text = event.widget.cget("text")
    if text == "=":
        if txt_on_screen.get().isdigit():
            value = int(txt_on_screen.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value = "Error"

        txt_on_screen.set(value)
        screen.update()

    elif text == " C ":
        txt_on_screen.set("")
        screen.update()

    else:
        txt_on_screen.set(txt_on_screen.get() + text)
        screen.update()

root.geometry("504x578+20+20")
root.resizable(False,False)
root.title("Calculator - tkinter")
root.iconbitmap("./calculator-icon.ico")

#screen display config
txt_on_screen = StringVar()
txt_on_screen.set("")      # initially blank
screen = Entry(root, textvariable=txt_on_screen, font="jetbrains 50 bold", bg="#77c593")
screen.pack(padx=10, pady=10, fill="both")

fr = Frame(root, bg="#1e3d59")

b = Button(fr, padx=10, pady=10, text="9", font="lucida 30 bold", bg="#ff6e40", foreground="white")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>", click)

b = Button(fr, padx=10, pady=10, text="8", font="lucida 30 bold", bg="#ff6e40", foreground="white")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>", click)

b = Button(fr, padx=10, pady=10, text="7", font="lucida 30 bold", bg="#ff6e40", foreground="white")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>", click)

b = Button(fr, padx=12, pady=10, text="=", font="lucida 30 bold", bg="#77c593")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>", click)

b = Button(fr, padx=5, pady=10, text=" C ", font="lucida 30 bold", bg="#77c593")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>", click)

fr.pack(fill="both")

fr = Frame(root, bg="#1e3d59")

b = Button(fr, padx=10, pady=10, text="6", font="lucida 30 bold", bg="#ff6e40", foreground="white")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>", click)

b = Button(fr, padx=10, pady=10, text="5", font="lucida 30 bold", bg="#ff6e40", foreground="white")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>", click)

b = Button(fr, padx=10, pady=10, text="4", font="lucida 30 bold", bg="#ff6e40", foreground="white")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>", click)

b = Button(fr, padx=15, pady=10, text="*", font="lucida 30 bold", bg="#ffc13b")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>", click)

b = Button(fr, padx=25, pady=10, text="/", font="lucida 30 bold", bg="#ffc13b")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>", click)

fr.pack(fill="both")

fr = Frame(root, bg="#1e3d59")

b = Button(fr, padx=10, pady=10, text="3", font="lucida 30 bold", bg="#ff6e40", foreground="white")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>", click)

b = Button(fr, padx=10, pady=10, text="2", font="lucida 30 bold", bg="#ff6e40", foreground="white")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>", click)

b = Button(fr, padx=10, pady=10, text="1", font="lucida 30 bold", bg="#ff6e40", foreground="white")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>", click)

b = Button(fr, padx=12, pady=10, text="+", font="lucida 30 bold", bg="#ffc13b")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>", click)

b = Button(fr, padx=24, pady=10, text="-", font="lucida 30 bold", bg="#ffc13b")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>", click)

fr.pack(fill="both")

fr = Frame(root, bg="#1e3d59")

b = Button(fr, padx=5, pady=10, text=" . ", font="lucida 30 bold", bg="#ff6e40")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>", click)

b = Button(fr, padx=10, pady=10, text="0", font="lucida 30 bold", bg="#ff6e40")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>", click)

b = Button(fr, padx=2, pady=10, text="00", font="lucida 30 bold", bg="#ff6e40")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>", click)

b = Button(fr, padx=7, pady=10, text="%", font="lucida 30 bold", bg="#ffc13b")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>", click)

b = Button(fr, padx=20, pady=10, text="  ", font="lucida 30 bold", bg="#ffc13b")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>", click)

fr.pack(fill="both")

root.mainloop()