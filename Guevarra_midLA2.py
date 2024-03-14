import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

class Cars(tk.Tk):
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
        self.bmw_frm.pack(side=LEFT)
        self.subaru_frm.pack(side = LEFT)
        self.chev_frm.pack(side=LEFT)
    def upgrades(self):
        upgrades_window = Upgrade(self.cars)

class Upgrade(tk.Toplevel):
    def __init__(self, cars):
        super().__init__()
        self.cars = cars
        print(cars)
        self.geometry('500x500')
        self.title('Upgrades')
        self.mainfrm = Frame(self)
        self.interior_frm = Frame(self.mainfrm)
        self.interiorfrmlblleft_frm = Frame(self.interior_frm)
        self.interiorfrmlblright_frm = Frame(self.interior_frm)
        self.interiorfrmchk_frm = Frame(self.interior_frm)
        self.exteriorfnsh_frm = Frame(self.mainfrm)
        self.exteriorfrmlblleft_frm = Frame(self.exteriorfnsh_frm)
        self.exteriorfrmlblright_frm = Frame(self.exteriorfnsh_frm)
        self.exteriorfrmrbd_frm = Frame(self.exteriorfnsh_frm)
        self.exterioroptn_frm = Frame(self.mainfrm)
        self.exteriorfrmoptnlblleft_frm = Frame(self.exterioroptn_frm)
        self.exteriorfrmoptnlblright_frm = Frame(self.exterioroptn_frm)
        self.interiorfrmoptnchk_frm = Frame(self.exterioroptn_frm)

        self.price1,self.price2,self.price3 = IntVar(),IntVar(),IntVar()

        upgr_list = (("leather", 550, -550),("GPS", 1000, -1000))

        self.interior1_lbl = Label(self.interiorfrmlblleft_frm, text="Interior Options")
        self.interior_lbl = Label(self.interiorfrmlblright_frm, text="leather")
        self.interior_chk = Checkbutton(self.interiorfrmchk_frm, variable=self.price1, onvalue= 550, offvalue= -550)
        self.interior2_lbl = Label(self.interiorfrmlblright_frm, text="GPS")
        self.interior2_chk = Checkbutton(self.interiorfrmchk_frm, variable=self.price2, onvalue= 1000, offvalue= -1000)

        self.exterior1_lbl_frm = Label(self.exteriorfrmlblleft_frm, text="Exterior Finish")
        self.exterior_lbl = Label(self.exteriorfrmlblright_frm, text="Hard Top")
        self.exterior_rdb = Radiobutton(self.exteriorfrmrbd_frm, variable=self.price2, value=0)
        self.exterior2_lbl = Label(self.exteriorfrmlblright_frm, text="Convertible")
        self.exterior2_rdb = Radiobutton(self.exteriorfrmrbd_frm, variable=self.price2, value=0)


        self.mainfrm.pack()
        self.interior_frm.pack()
        self.interiorfrmlblleft_frm.pack(side=LEFT)
        self.interiorfrmlblright_frm.pack()
        self.interiorfrmchk_frm.pack()
        self.exteriorfnsh_frm.pack()
        self.exteriorfrmlblleft_frm.pack(side=LEFT)
        self.exteriorfrmlblright_frm.pack()
        self.exteriorfrmrbd_frm.pack()
        self.exterioroptn_frm.pack()
        self.exteriorfrmoptnlblleft_frm.pack(side=LEFT)
        self.exteriorfrmoptnlblright_frm.pack()
        self.interiorfrmoptnchk_frm.pack()

        self.interior1_lbl.pack(padx=100)
        self.interior2_lbl.pack(side=RIGHT)
        self.interior_lbl.pack(side=RIGHT)
        self.interior2_chk.pack(side=RIGHT)
        self.interior_chk.pack(side=RIGHT)
        


        self.transient(self.master)
        self.grab_set()
        self.wait_window(self)



if __name__ == "__main__":
    car_upgrade = Cars()
    car_upgrade.mainloop()
