import tkinter as tk
from tkinter import ttk
from tkinter import *
import re

class EntryActivity(tk.Tk):
    def __init__(self):
        super().__init__()

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
                                     command= self.showentry)
        self.lbldsp = Label(self.dspfrm,
                            text= "Display")
        self.lbltxt = Label(self.dspfrm,
                            text="<Entered Word Appears Here>")
        
        self.mainfrm.pack(fill=tk.BOTH, expand= True)
        self.entfrm.grid()
        self.btnfrm.grid(column=1, row=1)
        self.dspfrm.grid(column=2, row=0)

        self.nmlbl.pack()
        self.entry_text.pack()
        self.button_display.pack()
        self.lbldsp.pack()
        self.lbltxt.pack()

    def showentry(self):
        print("Tite")
        text = self.entry_text.get()
        if text == "" or text == " ":
            print("Tits")
            self.lbltxt.configure(text="Enter a word")
        elif re.findall("\w \w", text):
            print("succubus")
            self.lbltxt.configure(text="Only one word is acceptable")
        else:
            print("Kantot")
            self.lbltxt.configure(text=text)
        


if __name__ == "__main__":
    main_window = EntryActivity()
    main_window.mainloop()
