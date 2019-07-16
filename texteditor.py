# A Basic Text Editor where you can Open and Save Files
from tkinter import *
from tkinter import filedialog
window = Tk()
def closeFile():
    window.destroy()
def openFile():
    try:
        t=filedialog.askopenfile(mode="r",title="Select File",filetypes=[("All Files","*.*")])
        content.insert(END,t.read())
    except:
        print("Cannot Open File")
    finally:
        t.close()
def saveFile():
    f = filedialog.asksaveasfile(mode="w",defaultextension=".txt")
    if f is None:
        return
    try:
        textuserinput=str(content.get(1.0,END))
        f.write(textuserinput)
    except:
        print("Cannot Save the File")
    finally:
        if t:
            f.close()
mainmenu = Menu(window)
window.config(menu=mainmenu)
filemenu = Menu(mainmenu)
mainmenu.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="Open",command=openFile)
filemenu.add_command(label="Save",command=saveFile)
filemenu.add_separator()
filemenu.add_command(label="Close",command=closeFile)
mainmenu.add_cascade(label="Help")
content = Text(window,width=100)
content.grid(row=0,column=0,padx=5,pady=5)
window.mainloop()