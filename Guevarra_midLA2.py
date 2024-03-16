import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter.messagebox import showinfo

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
            self.radio_car = Radiobutton(car[5], text=car[0], variable=car[4], value=car[3], command=self.upgrades, font=self.font, bg="#fff5d4", cursor= 'hand2')
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
        self.upgrades_window.chkhover()
        self.upgrades_window.chkhover2()
        self.upgrades_window.chkhover3()
        self.upgrades_window.chkhover4()
        

    


class Upgrade(tk.Toplevel):
    def __init__(self, cars, font, car_price):
        super().__init__()
        self.car_price = car_price
        print(self.car_price)
        self.font = font
        self.cars = cars
        self.list_upgr = [[self.car_price[0], self.car_price[1]]]
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

        self.price1,self.price2,self.price3,self.price4,self.price5 = StringVar(),StringVar(),StringVar(),StringVar(),StringVar()   
        self.price1.set("0.00")
        self.price2.set("0.00")
        self.price3.set("0.00")
        self.price4.set("0.00")
        self.price5.set("0.00")

        self.upgr_list = {"leather": 550, "GPS": 1000, "Wheel Upgrade": 1000, "Performance Package": 2000, self.car_price[0]: self.car_price[1], "Hard Top": 0, "Convertible": 0}
        print(self.upgr_list.keys())

        self.interior1_lbl = Label(self.interiorfrmlbltop_frm, text="Interior Options", bg="#aa6f73", padx=5, pady=5, font=self.font)
        self.interior_lbl = Label(self.interiorfrmlblbot_frm, text="leather", bg="#aa6f73", padx=5, pady=5, font=self.font)
        self.interior_chk = Checkbutton(self.interiorfrmlblbot_frm, variable=self.price1, onvalue= "leather", offvalue= "-leather", command=self.add, bg="#aa6f73", padx=5, pady=5)
        self.interior2_lbl = Label(self.interiorfrmlblbot_frm, text="GPS", bg="#aa6f73", padx=5, pady=5, font=self.font)
        self.interior2_chk = Checkbutton(self.interiorfrmlblbot_frm, variable=self.price2, onvalue= "GPS", offvalue= "-GPS", command=self.add2, bg="#aa6f73", padx=5, pady=5)

        self.exterior1_lbl_frm = Label(self.exteriorfrmlbltop_frm, text="Exterior Finish", bg="#aa6f73", padx=5, pady=5, font=self.font)
        self.exterior_lbl = Label(self.exteriorfrmlblbot_frm, text="Hard Top", bg="#aa6f73", padx=5, pady=5, font=self.font)
        self.exterior_rdb = Radiobutton(self.exteriorfrmlblbot_frm, variable=self.price3, value="Hard Top", command=self.add3, bg="#aa6f73", state=NORMAL, padx=5, pady=5)
        self.exterior2_lbl = Label(self.exteriorfrmlblbot_frm, text="Convertible", bg="#aa6f73", padx=5, pady=5, font=self.font)
        self.exterior2_rdb = Radiobutton(self.exteriorfrmlblbot_frm, variable=self.price3, value="Convertible", command=self.add3, bg="#aa6f73", state=NORMAL, padx=5, pady=5)

        self.exterioroptn_lbl = Label(self.exteriorfrmoptnlbltop_frm, text="Exterior Option", bg="#aa6f73", font=self.font)
        self.exterioroptn1_lbl = Label(self.exteriorfrmoptnlblbot_frm, text="Wheel Upgrade", bg="#aa6f73", font=self.font)
        self.exterioroptn_chk = Checkbutton(self.exteriorfrmoptnlblbot_frm, variable=self.price4, onvalue="Wheel Upgrade", offvalue="-Wheel Upgrade", command=self.add4, bg="#aa6f73")
        self.exterioroptn2_lbl = Label(self.exteriorfrmoptnlblbot_frm, text="Performance Package", bg="#aa6f73", font=self.font)
        self.exterioroptn2_chk = Checkbutton(self.exteriorfrmoptnlblbot_frm, variable=self.price5, onvalue="Performance Package", offvalue="-Performance Package", command=self.add5, bg="#aa6f73")

        self.checkout_btn = Button(self.cheeckoutbtn_frm, text="Checkout", font=self.font, background="#efc6c6", cursor="hand2", command=self.checkout)

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
        
        self.protocol("WM_DELETE_WINDOW", self.confirm)
        self.transient(self.master)
        self.grab_set()
        

    def add(self):
        if self.price1.get() in self.upgr_list.keys():
            print(self.price1.get())
            if self.price1.get() not in self.list_upgr:
                self.list_upgr.append([self.price1.get(), self.upgr_list.get(self.price1.get())])
        elif self.price1.get() in "-"+self.price1.get():
            print("nigger")
            pricepop = self.price1.get()
            pricepopfinal = pricepop.replace("-", "")
            carvalue_list = [pricepopfinal, self.upgr_list.get(pricepopfinal)]
            print(carvalue_list)
            for index, list_to_find in enumerate(self.list_upgr):
                if list_to_find == carvalue_list:
                    print(index)
                    self.list_upgr.pop(index)
                    break
            
            
    def add2(self):
        if self.price2.get() in self.upgr_list.keys():
            print(self.price2.get())
            if self.price2.get() not in self.list_upgr:
                self.list_upgr.append([self.price2.get(), self.upgr_list.get(self.price2.get())])
        elif self.price2.get() in "-"+self.price2.get():
            print("nigger")
            pricepop = self.price2.get()
            pricepopfinal = pricepop.replace("-", "")
            carvalue_list = [pricepopfinal, self.upgr_list.get(pricepopfinal)]
            print(carvalue_list)
            for index, list_to_find in enumerate(self.list_upgr):
                if list_to_find == carvalue_list:
                    print(index)
                    self.list_upgr.pop(index)
                    break

    def add3(self): 
        print(f"Niggas in: {self.price3.get()}")       
        
        if ["Convertible", 0] in self.list_upgr:
            print(f"nigga {self.price3.get()}")
            for index, list_to_find in enumerate(self.list_upgr):
                if list_to_find == ["Convertible", 0]:
                    print("NIGGA FOUND")
                    self.list_upgr.pop(index)
                    self.list_upgr.append([self.price3.get(), self.upgr_list.get(self.price3.get())])
                    break
        elif ["Hard Top", 0] in self.list_upgr:
            for index, list_to_find in enumerate(self.list_upgr):
                if list_to_find == ["Hard Top", 0]:
                    print("NIGGER FOUND")
                    self.list_upgr.pop(index)
                    self.list_upgr.append([self.price3.get(), self.upgr_list.get(self.price3.get())])
                    break    
        else:
            self.list_upgr.append([self.price3.get(), self.upgr_list.get(self.price3.get())])

    def add4(self):
        if self.price4.get() in self.upgr_list.keys():
            print(self.price4.get())
            self.list_upgr.append([self.price4.get(), self.upgr_list.get(self.price4.get())])
        elif self.price4.get() in "-"+self.price4.get():
            print("nigger")
            pricepop = self.price4.get()
            pricepopfinal = pricepop.replace("-", "")
            carvalue_list = [pricepopfinal, self.upgr_list.get(pricepopfinal)]
            print(carvalue_list)
            for index, list_to_find in enumerate(self.list_upgr):
                if list_to_find == carvalue_list:
                    print(index)
                    self.list_upgr.pop(index)
                    break
    
    def add5(self):
        if self.price5.get() in self.upgr_list.keys():
            print(self.price5.get())
            self.list_upgr.append([self.price5.get(), self.upgr_list.get(self.price5.get())])
        elif self.price5.get() in "-"+self.price5.get():
            print("nigger")
            pricepop = self.price5.get()
            pricepopfinal = pricepop.replace("-", "")
            carvalue_list = [pricepopfinal, self.upgr_list.get(pricepopfinal)]
            print(carvalue_list)
            for index, list_to_find in enumerate(self.list_upgr):
                if list_to_find == carvalue_list:
                    print(index)
                    self.list_upgr.pop(index)
                    break

    def rdbhover(self):
        self.exterior_rdb.bind("<Enter>", func= lambda e: self.exterior_rdb.configure(
            background = "#c2c3ff",
            cursor= "hand2"
        ))
        self.exterior_rdb.bind("<Leave>", func= lambda e: self.exterior_rdb.configure(
            background = "#aa6f73",
            cursor= "hand2"
        ))


    def rdbhover2(self):
        self.exterior2_rdb.bind("<Enter>", func= lambda e: self.exterior2_rdb.configure(
            background = "#c2c3ff",
            cursor= "hand2"
        ))
        self.exterior2_rdb.bind("<Leave>", func= lambda e: self.exterior2_rdb.configure(
            background = "#aa6f73",
            cursor= "hand2"
        ))
    
    def chkhover(self):
        self.interior_chk.bind("<Enter>", func= lambda e: self.interior_chk.configure(
            background = "#c2c3ff",
            cursor= "hand2"
        ))
        self.interior_chk.bind("<Leave>", func= lambda e: self.interior_chk.configure(
            background = "#aa6f73",
            cursor= "hand2"
        ))


    def chkhover2(self):
        self.interior2_chk.bind("<Enter>", func= lambda e: self.interior2_chk.configure(
            background = "#c2c3ff",
            cursor= "hand2"
        ))
        self.interior2_chk.bind("<Leave>", func= lambda e: self.interior2_chk.configure(
            background = "#aa6f73",
            cursor= "hand2"
        ))
        
    
    def chkhover3(self):
        print("Hovered+")
        self.exterioroptn2_chk.bind("<Enter>", func= lambda e: self.exterioroptn2_chk.configure(
            background = "#c2c3ff",
            cursor= "hand2"
        ))
        self.exterioroptn2_chk.bind("<Leave>", func= lambda e: self.exterioroptn2_chk.configure(
            background = "#aa6f73",
            cursor= "hand2"
        ))


    def chkhover4(self):
        print("Hovered+")
        self.exterioroptn_chk.bind("<Enter>", func= lambda e: self.exterioroptn_chk.configure(
            background = "#c2c3ff",
            cursor= "hand2"
        ))
        self.exterioroptn_chk.bind("<Leave>", func= lambda e: self.exterioroptn_chk.configure(
            background = "#aa6f73",
            cursor= "hand2"
        ))
        self.wait_window(self)
        
    def loopycheck(self):
        for i in len(self.list_upgr):
            return f"{self.list_upgr[i][0]} - {self.list_upgr[i][1]} \n"

    def checkout(self):
        checkout = Checkout(self.list_upgr, self.font)
        self.destroy


    def confirm(self):
        print('Done')
        print(self.list_upgr)
        self.list_upgr.clear()
        print(self.list_upgr)
        self.destroy()

class Checkout(Toplevel):
    def __init__(self, list, font):
        super().__init__()
        self.sumlist = []
        self.font = font
        self.list = list
        self.title("Checkout")
        self.geometry("500x600")
        self.minsize(500, 600)
        self.configure(bg='#d8eeff')

        self.main_frm = Frame(self, bg='#e5ffe1', highlightbackground='#ffd2d2', highlightthickness=1.5)
        self.top_frm = Frame(self.main_frm, bg='#e5ffe1')
        self.bot_frm = Frame(self.main_frm, bg='#e5ffe1')
        self.totalbot_frm = Frame(self.main_frm, bg='#e5ffe1')
        self.right_frm = Frame(self.bot_frm, bg='#e5ffe1')
        self.left_frm = Frame(self.bot_frm, bg='#e5ffe1')
        self.Checkouttop_lbl = Label(self.top_frm, text="Car Upgrades:", anchor='center', justify='center', bg='#e5ffe1', font=self.font)
        for i in range(len(self.list)):
            self.Checkoutbotleft_lbl = Label(self.left_frm, text=f"{self.list[i][0]}:", bg='#e5ffe1', font=self.font)
            self.Checkoutbotleft_lbl.pack(padx=5, pady=5, anchor='center')
        for i in range(len(self.list)):
            self.Checkoutbotright_lbl = Label(self.right_frm, text=f"{self.list[i][1]}", bg='#e5ffe1', font=self.font)
            self.Checkoutbotright_lbl.pack(padx=5, pady=5, anchor='center')
        for i in range(len(self.list)):
            self.sumlist.append(self.list[i][1])
        summer = sum(self.sumlist)
        self.total_lbl = Label(self.totalbot_frm, text=f"Total is: {summer}", anchor='center', justify='center', bg='#ffe4d2', font=self.font)

        self.Checkouttop_lbl.pack(padx=5, pady=5, anchor='center')
        self.main_frm.pack(pady=100)
        self.top_frm.pack(side= TOP)
        self.totalbot_frm.pack(side=BOTTOM)
        self.bot_frm.pack(side= BOTTOM)
        self.right_frm.pack(side= RIGHT)
        self.left_frm.pack(side= LEFT)
        
        self.total_lbl.pack(side=BOTTOM)

        self.transient(self.master)
        self.grab_set()
        self.wait_window(self)
        



if __name__ == "__main__":
    main_wdw = Cars()
    main_wdw.mainloop()
