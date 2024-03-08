import tkinter as tk
from tkinter import ttk
from tkinter import *
import re

class EntryActivity(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("J1T-midLA1")
        self.geometry("600x500")
        self.minsize(600, 400)
        self.font = ("Comic Sans MS", 15, "bold")
        self.configure(cursor="arrow", background="#6D6875")
        self.mainfrm = Frame(self, highlightbackground="#FFCDB2", highlightthickness=1.5, borderwidth=20, background="#B5838D")
        self.entfrm = Frame(self.mainfrm, highlightbackground="#FFCDB2", highlightthickness=1.5, borderwidth=5, background="#E5989B")
        self.btnfrm = Frame(self.mainfrm, highlightbackground="#FFCDB2", highlightthickness=1.5, borderwidth=5, background="#E5989B")
        self.dspfrm = Frame(self.mainfrm, highlightbackground="#FFCDB2", highlightthickness=1.5, background="#FFB4A2")

        self.nmlbl = Label(self.entfrm,
                           text = "Lucky Angel",
                           background="#E5989B",
                           font= self.font)
        self.entry_text = Entry(self.entfrm,
                                width=25,
                                font= self.font)
        self.entry_text.insert(0, "Input a Text")
        self.entry_text.bind("<FocusIn>", self.temp_text)
        
        self.button_display = Button(self.btnfrm,
                                     text= "Display Text",
                                     cursor="hand2",
                                     command= self.showentry,
                                     background="#FDF0C2",
                                     font= self.font)
        self.lbldsp = Label(self.dspfrm,
                            text= "Display:",
                            background="#FFB4A2",
                            font= self.font)
        self.label_txt = Label(self.dspfrm,
                               text="", wraplength=100,
                               background="#FFB4A2",
                               font= self.font)
        
        self.mainfrm.pack(expand=True)
        self.entfrm.pack(side=LEFT, expand=True, padx=50)
        self.btnfrm.pack(side= BOTTOM, expand=True)
        self.dspfrm.pack(side=RIGHT, expand=True, pady=25)

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
           highlightbackground="#FFCDB2"
       ))
       self.button_display.bind("<Leave>", func=lambda e: self.button_display.configure(
           relief= RAISED,
           highlightbackground="#FFCDB2"
       ))
    def enthover(self):
        self.entry_text.bind("<Enter>", func= lambda e: self.entry_text.configure(
            relief= RIDGE,
            highlightbackground="#FFCDB2"
        ))
        self.entry_text.bind("<Leave>", func=lambda e:self.entry_text.configure(
            relief= SUNKEN,
            highlightbackground="#FFCDB2"
        ))
    def dsphover(self):
        self.label_txt.bind("<Enter>", func= lambda e: self.label_txt.configure(
            fg="blue",
        ))
        self.label_txt.bind("<Leave>", func= lambda e: self.label_txt.configure(
            fg="black"
        ))
    def temp_text(self, e):
        self.entry_text.delete(0, "end")
    

    


if __name__ == "__main__":
    main_window = EntryActivity()
    main_window.buttonhover()
    main_window.enthover()
    main_window.dsphover()
    main_window.mainloop()
