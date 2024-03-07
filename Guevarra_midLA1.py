import tkinter as tk
from tkinter import ttk
from tkinter import *
import re

class EntryActivity(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("J1T-midLA1")
        self.geometry("500x500")
        self.configure(cursor="arrow")
        self.mainfrm = Frame(self)
        self.entfrm = Frame(self.mainfrm)
        self.btnfrm = Frame(self.mainfrm)
        self.dspfrm = Frame(self.mainfrm)

        self.nmlbl = Label(self.entfrm,
                           text = "Lucky Angel")
        self.entry_text = Entry(self.entfrm,
                                width=25)
        
        self.button_display = Button(self.btnfrm,
                                     text= "Display Text",
                                     cursor="hand2",
                                     command= self.showentry)
        self.lbldsp = Label(self.dspfrm,
                            text= "Display")
        self.label_txt = Label(self.dspfrm,
                               text="", wraplength=100)
        
        self.mainfrm.pack(anchor=CENTER, pady=150)
        self.entfrm.grid()
        self.btnfrm.grid(column=1, row=1)
        self.dspfrm.grid(column=2, row=0)

        self.nmlbl.pack()
        self.entry_text.pack()
        self.button_display.pack()
        self.lbldsp.pack()
        self.label_txt.pack()

    def showentry(self):
        text = self.entry_text.get()
        if text == "" or text == " ":
            self.label_txt.configure(text="Enter a word")
        elif re.findall("\w \w", text):
            self.label_txt.configure(text="Only one word is acceptable")
        else:
            self.label_txt.configure(text=text)

    def buttonhover(self):
       self.button_display.bind("<Enter>", func=lambda e: self.button_display.configure(
           relief= GROOVE,
           #bd= 5
       ))
       self.button_display.bind("<Leave>", func=lambda e: self.button_display.configure(
           relief= RAISED,
           #bd= 2
       ))
    def enthover(self):
        self.entry_text.bind("<Enter>", func= lambda e: self.entry_text.configure(
            relief= RIDGE,
            #bd= 5
        ))
        self.entry_text.bind("<Leave>", func=lambda e:self.entry_text.configure(
            relief= SUNKEN,
            #bd=2
        ))
    def dsphover(self):
        self.label_txt.bind("<Enter>", func= lambda e: self.label_txt.configure(
            fg="blue",
        ))
        self.label_txt.bind("<Leave>", func= lambda e: self.label_txt.configure(
            fg="black"
        ))
    

    


if __name__ == "__main__":
    main_window = EntryActivity()
    main_window.buttonhover()
    main_window.enthover()
    main_window.dsphover()
    main_window.mainloop()
