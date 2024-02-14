import re
import random
Open = 1
class BankAccount():
    def __init__(self, username, password, account_number, account_holder, balance):
        self.username = username
        self.password = password
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = int(balance)
        self.ask()
    def ask(self):
        while True:
            choose = input("Diplay info | Deposit | Withdraw | Get Balance\n Choose: ")
            if choose.lower() == "display info":
                self.display_info()
                break
            elif choose.lower() == "deposit":
                self.deposit()
                break
            elif choose.lower() == "withdraw":
                self.withdraw()
                break
            elif choose.lower() == "get balance":
                self.get_balance()
                break
    def display_info(self):
        print(f"Account Number: {self.account_number} \nAccount Holder: {self.account_holder} \nBalance: {self.balance}")
        self.ask()
    def display_info2(self):
        print(f"Account Number: {self.account_number} \nAccount Holder: {self.account_holder} \nBalance: {self.balance}")
    def deposit(self):
        amount = int(input("Enter Amount to deposit: "))
        self.display_info2()
        self.balance = amount + self.balance
        print(f"Deposit of ${amount} successful.\nCurrent Balance: ${self.balance}") #sorry if it doesnt include the decimals in the whole program as I can't really detect . in regex
        databank[self.username] = f"{self.password}, {self.account_number}, {self.account_holder}, {self.balance}"
        Exit()
    def withdraw(self):
        amount = int(input("Enter Amoung to withdraw: "))
        self.display_info2()
        self.balance = self.balance - amount
        print(f"Withdrawal of ${amount} successful.\nCurrent Balance: ${self.balance}")
        databank[self.username] = f"{self.password}, {self.account_number}, {self.account_holder}, {self.balance}"
        Exit()
    def get_balance(self):
        print(f"Current balance is: ${self.balance}")
        self.ask()

class Login():
    def __init__(self):
        self.username = input("Enter Username: ")
        self.password = input("Enter Passowrd: ")
        self.verify()
        
    def verify(self):
        if self.username in databank.keys():
            information = databank[self.username].split(", ")
            if self.password in information[0]:
                BankAccount(self.username, information[0], information[1], information[2], information[3])


class Register():
    def __init__(self):
        self.username = input("Enter username: ")
        self.password = input("Enter password: ")
        self.bank_number = str(round(random.uniform(1,9)))+str(round(random.uniform(0,9)))+str(round(random.uniform(0,9)))+str(round(random.uniform(0,9)))+str(round(random.uniform(0,9)))+str(round(random.uniform(0,9)))+str(round(random.uniform(0,9)))+str(round(random.uniform(0,9)))+str(round(random.uniform(0,9)))+str(round(random.uniform(0,9)))
        self.bank_holder = input("Enter name(use underscore for space):")# I have not figured a way to include space and symbols in regex
        self.balance = 0
        self.submit()
    def submit(self):
        databank[self.username] = self.password + ", " + self.bank_number + ", " + self.bank_holder + ", " + str(self.balance)
        print(databank)
        Login()


class Starting():
    def __init__(self):
        self.checkdata()
    
    def checkdata(self):
        while True:
            if open("bankdata.txt", "r"):
                bankdata = open("bankdata.txt", "r").read()
            else:
                bankdata = open("databank.txt", "x")
                Register()
                break
            self.data = bankdata
            self.retreive()
            break
        self.retreive()
    def retreive(self):
        split = re.findall("\w+", self.data)
        for i in range(len(split)):
            for j in range(5):
                listinitialized.append(split[0])
                split.pop(0)
            databank[listinitialized[0]] = listinitialized[1] + ", " + listinitialized[2] + ", " + listinitialized[3] + ", " + listinitialized[4]
        self.ask()
    def ask(self):
        while True:  
            asked = input("Login or Register: ")  
            if asked.lower() == "login":
                Login()
                break
            elif asked.lower() == "register":
                Register()
                break

def cclose():
    global Open
    Open = 0

class Exit():
    def __init__(self):
        self.exiting()
    def exiting(self):
        datakeys = list(databank.keys())
        for i in range(len(datakeys)):
            listoput.append(datakeys[i]+", "+databank[datakeys[i]])
        f = open("bankdata.txt", "w")
        f.write(str(listoput))
        f.close()
        cclose()



databank = {}
listoput = []
listinitialized = []
while Open == 1:
    Starting()
    break
