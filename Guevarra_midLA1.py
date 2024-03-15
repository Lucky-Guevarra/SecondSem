import tkinter as tk
from tkinter import *
from tkinter.messagebox import askyesno
from PIL import ImageTk, Image

class Cars(Tk):
    def __init__(self):
        super().__init__()
        self.title("J1T-midLA2")
        self.geometry("500x500")
        self.minsize(500, 500)
        self.font = ("Comic Sans MS", 15)
        self.configure(background='#FFCDB2')

        self.mainfrm = Frame(self)
        self.car_frm = Frame(self.mainfrm, background='#FFCDB2')
        self.bmw_frm, self.subaru_frm, self.chev_frm = Frame(self.car_frm, background='#FFCDB2'), Frame(self.car_frm, background='#FFCDB2'), Frame(self.car_frm, background='#FFCDB2')

        self.carprice1 = IntVar()

        self.bmwlogo = ImageTk.PhotoImage(Image.open('BMW_LOGO.png'))
        self.chevlogo = ImageTk.PhotoImage(Image.open('CHEVROLET_LOGO.png'))
        self.subalogo = ImageTk.PhotoImage(Image.open('SUBARU_LOGO.png'))

        self.bmwcar  = ImageTk.PhotoImage(Image.open('BMW_CAR.png'))
        self.chevcar = ImageTk.PhotoImage(Image.open('CHEVROLET_CAR.png'))
        self.subacar = ImageTk.PhotoImage(Image.open('SUBARU_CAR.png'))

        cars = (("BMW", self.bmwlogo, self.bmwcar, 5000.00, self.carprice1, self.bmw_frm, 15,45, 0, 10),
                ("CHEVROLET", self.chevlogo, self.chevcar, 4100.00, self.carprice1, self.chev_frm, 50, 30, 20, 5),
                ("SUBARU", self.subalogo, self.subacar, 2500.00, self.carprice1, self.subaru_frm, 50, 30, 20, 10))
        self.cars = cars
        for car in cars:
            print("chigga")
            self.logo = car[1]
            self.car = car[2]
            self.logo1 = Label(car[5], image=self.logo, background='#FFCDB2')
            self.radio_car = Radiobutton(car[5], text=car[0], variable=car[4], value=car[3], command=self.upgrades, font=self.font)
            self.car1 = Label(car[5], image=self.car, background='#FFCDB2') 
            self.logo1.pack(pady = car[6], padx=car[9])
            self.radio_car.pack(pady= car[7], padx=car[9])
            self.car1.pack(pady= car[8], padx=car[9])
            print("Chigga Done")
        

        self.mainfrm.pack()
        self.car_frm.pack()
        self.bmw_frm.pack(side='left')
        self.subaru_frm.pack(side = 'left')
        self.chev_frm.pack(side="left")
        
        

    def upgrades(self):
        self.car_price = self.carprice1.get()
        if self.car_price == 5000:
            self.car = ("BMW", self.car_price)
        elif self.car_price == 4000:
            self.car = ("Chevrolet", self.car_price)
        else:
            self.car = ("Subaru", self.car_price)
        self.upgrades_window = Upgrade(cars= self.cars, font= self.font, car_price= self.car)
        self.upgrades_window.rdbhover()
        self.upgrades_window.rdbhover2()

    


class Upgrade(tk.Toplevel):
    def __init__(self, cars, font, car_price):
        super().__init__()
        self.car_price = car_price
        print(self.car_price)
        self.font = font
        self.cars = cars
        print(self.cars)
        self.geometry('500x600')
        self.minsize(500, 600)
        self.title('Upgrades')
        self.configure(bg='#f6e0b5')
        self.mainfrm = Frame(self, bg="#f6e0b5")
        self.interior_frm = Frame(self.mainfrm, bg="#aa6f73", highlightbackground="#9aa0a3", highlightthickness=2)
        self.interiorfrmlbltop_frm = Frame(self.interior_frm, bg="#aa6f73")
        self.interiorfrmlblbot_frm = Frame(self.interior_frm, bg="#aa6f73")
        self.exteriorfnsh_frm = Frame(self.mainfrm, bg="#aa6f73", highlightbackground='#9aa0a3', highlightthickness=2)
        self.exteriorfrmlbltop_frm = Frame(self.exteriorfnsh_frm, bg="#aa6f73")
        self.exteriorfrmlblbot_frm = Frame(self.exteriorfnsh_frm, bg="#aa6f73")
        self.exterioroptn_frm = Frame(self.mainfrm, bg="#aa6f73", highlightbackground='#9aa0a3', highlightthickness=2)
        self.exteriorfrmoptnlbltop_frm = Frame(self.exterioroptn_frm, bg="#aa6f73")
        self.exteriorfrmoptnlblbot_frm = Frame(self.exterioroptn_frm, bg="#aa6f73")
        self.cheeckoutbtn_frm = Frame(self.mainfrm, bg="#aa6f73")

        self.price1,self.price2,self.price3,self.price4,self.price5, self.price6 = IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar()

        upgr_list = (("leather", 550, -550),("GPS", 1000, -1000))

        self.interior1_lbl = Label(self.interiorfrmlbltop_frm, text="Interior Options", bg="#aa6f73", padx=5, pady=5, font=self.font)
        self.interior_lbl = Label(self.interiorfrmlblbot_frm, text="leather", bg="#aa6f73", padx=5, pady=5, font=self.font)
        self.interior_chk = Checkbutton(self.interiorfrmlblbot_frm, variable=self.price1, onvalue= 550, offvalue= -550, bg="#aa6f73", padx=5, pady=5)
        self.interior2_lbl = Label(self.interiorfrmlblbot_frm, text="GPS", bg="#aa6f73", padx=5, pady=5, font=self.font)
        self.interior2_chk = Checkbutton(self.interiorfrmlblbot_frm, variable=self.price2, onvalue= 1000, offvalue= -1000, bg="#aa6f73", padx=5, pady=5)

        self.exterior1_lbl_frm = Label(self.exteriorfrmlbltop_frm, text="Exterior Finish", bg="#aa6f73", padx=5, pady=5, font=self.font)
        self.exterior_lbl = Label(self.exteriorfrmlblbot_frm, text="Hard Top", bg="#aa6f73", padx=5, pady=5, font=self.font)
        self.exterior_rdb = Radiobutton(self.exteriorfrmlblbot_frm, variable=self.price3, value=1, bg="#aa6f73", state=NORMAL, padx=5, pady=5)
        self.exterior2_lbl = Label(self.exteriorfrmlblbot_frm, text="Convertible", bg="#aa6f73", padx=5, pady=5, font=self.font)
        self.exterior2_rdb = Radiobutton(self.exteriorfrmlblbot_frm, variable=self.price3, value=2, bg="#aa6f73", state=NORMAL, padx=5, pady=5)

        self.exterioroptn_lbl = Label(self.exteriorfrmoptnlbltop_frm, text="Exterior Option", bg="#aa6f73", font=self.font)
        self.exterioroptn1_lbl = Label(self.exteriorfrmoptnlblbot_frm, text="Wheel Upgrade", bg="#aa6f73", font=self.font)
        self.exterioroptn_chk = Checkbutton(self.exteriorfrmoptnlblbot_frm, variable=self.price5, onvalue=1000, offvalue=-1000, bg="#aa6f73")
        self.exterioroptn2_lbl = Label(self.exteriorfrmoptnlblbot_frm, text="Performance Package", bg="#aa6f73", font=self.font)
        self.exterioroptn2_chk = Checkbutton(self.exteriorfrmoptnlblbot_frm, variable=self.price6, onvalue=2000, offvalue=-2000, bg="#aa6f73")

        self.checkout_btn = Button(self.cheeckoutbtn_frm, text="Checkout", font=self.font, background="#efc6c6", cursor="hand2")

        self.mainfrm.pack()
        self.interior_frm.pack(padx=50, pady=50)
        self.interiorfrmlbltop_frm.pack(side="top")
        self.interiorfrmlblbot_frm.pack(side='bottom')
        self.exteriorfnsh_frm.pack(padx=50, pady=25)
        self.exteriorfrmlbltop_frm.pack(side="top")
        self.exteriorfrmlblbot_frm.pack(side='bottom')
        self.exterioroptn_frm.pack(pady=25)
        self.exteriorfrmoptnlbltop_frm.pack(side="top")
        self.exteriorfrmoptnlblbot_frm.pack(side="bottom")

        self.interior1_lbl.pack(padx=100)
        self.interior2_lbl.pack(side="right")
        self.interior2_chk.pack(side="right")
        self.interior_chk.pack(side="right")
        self.interior_lbl.pack(side="right")

        self.exterior1_lbl_frm.pack(padx= 100)
        self.exterior_lbl.pack(side='right')
        self.exterior_rdb.pack(side='right')
        self.exterior2_rdb.pack(side='right')
        self.exterior2_lbl.pack(side='right')

        self.exterioroptn_lbl.pack(padx=100)
        self.exterioroptn1_lbl.pack(side='right')
        self.exterioroptn_chk.pack(side='right')
        self.exterioroptn2_chk.pack(side='right')
        self.exterioroptn2_lbl.pack(side='right')

        self.cheeckoutbtn_frm.pack(pady=10)
        self.checkout_btn.pack()

    def rdbhover(self):
        print("Hovered+")
        self.exterior_rdb.bind("<Enter>", func= lambda e: self.exterior_rdb.configure(
            background = "#c2c3ff",
            cursor= "hand2"
        ))
        self.exterior_rdb.bind("<Leave>", func= lambda e: self.exterior_rdb.configure(
            background = "#aa6f73",
            cursor= "hand2"
        ))


    def rdbhover2(self):
        print("Hovered+")
        self.exterior2_rdb.bind("<Enter>", func= lambda e: self.exterior2_rdb.configure(
            background = "#c2c3ff",
            cursor= "hand2"
        ))
        self.exterior2_rdb.bind("<Leave>", func= lambda e: self.exterior2_rdb.configure(
            background = "#aa6f73",
            cursor= "hand2"
        ))


        
        self.protocol("WM_DELETE_WINDOW", self.confirm)
        self.transient(self.master)
        self.grab_set()
        self.wait_window(self)
        

    def confirm(self):
        print("confirmed")
        self.destroy()

    


if __name__ == "__main__":
    main_wdw = Cars()
    main_wdw.mainloop()
