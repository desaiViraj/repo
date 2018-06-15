import tkinter
import tkinter.filedialog

def NewFile():
    print("New File")

def OpenFile():
    name = askopenfilename()
    print(name)

def About():
    print("This is a simple example")

root = tkinter.Tk()
root.geometry("622x356")
root.title("File Menu")
menu = tkinter.Menu()
root.config(menu=menu)
filemenu = tkinter.Menu(menu)
menu.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="New",command=NewFile)
filemenu.add_command(label="Open",command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=root.quit)

helpmenu = tkinter.Menu(menu)
menu.add_cascade(label="Help",menu=helpmenu)
helpmenu.add_cascade(label="About",command=About)

root.mainloop()
