from tkinter import *
from tkinter import filedialog
import os
 
root = Tk()
root.title('Browse File')
root.geometry('350x320')
root.config(bg='lightblue')
 
def browse_files():
    file_gui = filedialog.askopenfilenames()
    
    for i in file_gui :
        gui_filename = os.path.basename(i)
        only_name = gui_filename.split(".")
        listbox_1.insert(END,only_name[0])
 
listbox_1 = Listbox(root,width=15,height=4)
listbox_1.place(x=50,y=70)
 
button_1 = Button(root,text='Open File',command=browse_files)
button_1.config(width=10,height=4)
button_1.place(x=220,y=70)

button_2 = Button(root,text='Generate',command=browse_files)
button_2.config(width=10,height=4)
button_2.place(x=120,y=180)
 
root.resizable(False,False)
root.mainloop()