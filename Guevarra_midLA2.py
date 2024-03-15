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

        cars = (("BMW", self.bmwlogo, self.bmwcar, 5000.00, self.carprice1, self.bmw_frm, 15,45, 0),
                ("CHEVROLET", self.chevlogo, self.chevcar, 4100.00, self.carprice1, self.chev_frm, 50, 30, 20),
                ("SUBARU", self.subalogo, self.subacar, 2500.00, self.carprice1, self.subaru_frm, 50, 30, 20))
        self.cars = cars
        for car in cars:
            print("chigga")
            self.logo = car[1]
            self.car = car[2]
            self.logo1 = Label(car[5], image=self.logo, background='#FFCDB2')
            self.radio_car = Radiobutton(car[5], text=car[0], variable=car[4], value=car[3], command=self.upgrades)
            self.car1 = Label(car[5], image=self.car, background='#FFCDB2') 
            self.logo1.pack(pady = car[6])
            self.radio_car.pack(pady= car[7])
            self.car1.pack(pady= car[8])
            print("Chigga Done")
        

        self.mainfrm.pack()
        self.car_frm.pack()
        self.bmw_frm.pack(side='left')
        self.subaru_frm.pack(side = 'left')
        self.chev_frm.pack(side="left")
        

    def upgrades(self):
        self.upgrades_window = Upgrade(self.cars)

    


class Upgrade(tk.Toplevel):
    def __init__(self, cars):
        super().__init__()
        self.cars = cars
        print(cars)
        self.geometry('500x500')
        self.title('Upgrades')
        self.configure(bg='#f6e0b5')
        self.mainfrm = Frame(self, bg="#f6e0b5")
        self.interior_frm = Frame(self.mainfrm, bg="#aa6f73", borderwidth=1,highlightbackground="#9aa0a3", highlightthickness=2,pady=50)
        self.interiorfrmlbltop_frm = Frame(self.interior_frm)
        self.interiorfrmlblbot_frm = Frame(self.interior_frm)
        self.exteriorfnsh_frm = Frame(self.mainfrm, bg="#aa6f73", borderwidth=10, highlightbackground='#9aa0a3', highlightthickness=2, pady=25)
        self.exteriorfrmlbltop_frm = Frame(self.exteriorfnsh_frm)
        self.exteriorfrmlblbot_frm = Frame(self.exteriorfnsh_frm)
        self.exterioroptn_frm = Frame(self.mainfrm, bg="#aa6f73", highlightbackground='#9aa0a3', highlightthickness=2, pady=25)
        self.exteriorfrmoptnlbltop_frm = Frame(self.exterioroptn_frm)
        self.exteriorfrmoptnlblbot_frm = Frame(self.exterioroptn_frm)

        self.price1,self.price2,self.price3,self.price4,self.price5 = IntVar(),IntVar(),IntVar(),IntVar(),IntVar()

        upgr_list = (("leather", 550, -550),("GPS", 1000, -1000))

        self.interior1_lbl = Label(self.interiorfrmlbltop_frm, text="Interior Options", bg="#aa6f73")
        self.interior_lbl = Label(self.interiorfrmlblbot_frm, text="leather", bg="#aa6f73")
        self.interior_chk = Checkbutton(self.interiorfrmlblbot_frm, variable=self.price1, onvalue= 550, offvalue= -550)
        self.interior2_lbl = Label(self.interiorfrmlblbot_frm, text="GPS", bg="#aa6f73")
        self.interior2_chk = Checkbutton(self.interiorfrmlblbot_frm, variable=self.price2, onvalue= 1000, offvalue= -1000)

        self.exterior1_lbl_frm = Label(self.exteriorfrmlbltop_frm, text="Exterior Finish", bg="#aa6f73")
        self.exterior_lbl = Label(self.exteriorfrmlblbot_frm, text="Hard Top", bg="#aa6f73")
        self.exterior_rdb = Radiobutton(self.exteriorfrmlblbot_frm, variable=self.price3, value=0)
        self.exterior2_lbl = Label(self.exteriorfrmlblbot_frm, text="Convertible", bg="#aa6f73")
        self.exterior2_rdb = Radiobutton(self.exteriorfrmlblbot_frm, variable=self.price3, value=0)

        self.exterioroptn_lbl = Label(self.exteriorfrmoptnlbltop_frm, text="Exterior Option", bg="#aa6f73")
        self.exterioroptn1_lbl = Label(self.exteriorfrmoptnlblbot_frm, text="Wheel Upgrade", bg="#aa6f73")
        self.exterioroptn_chk = Checkbutton(self.exteriorfrmoptnlblbot_frm, variable=self.price4, onvalue=1000, offvalue=-1000)
        self.exterioroptn2_lbl = Label(self.exteriorfrmoptnlblbot_frm, text="Performance Package", bg="#aa6f73")
        self.exterioroptn2_chk = Checkbutton(self.exteriorfrmoptnlblbot_frm, variable=self.price5, onvalue=2000, offvalue=-2000)

        self.mainfrm.pack()
        self.interior_frm.pack(padx=50)
        self.interiorfrmlbltop_frm.pack(side="top")
        self.interiorfrmlblbot_frm.pack(side='bottom')
        self.exteriorfnsh_frm.pack(padx=50)
        self.exteriorfrmlbltop_frm.pack(side="top")
        self.exteriorfrmlblbot_frm.pack(side='bottom')
        self.exterioroptn_frm.pack()
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
