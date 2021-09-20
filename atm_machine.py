class ATM_Machine:

    name = ""
    account = 0
    type = ""
    amount = 0
    total = 0
    avail_bal = 0

    def getData(self):
        try:
            self.name = input("Please enter your name : ")
            self.type = input("Please enter your account type : ")
            self.account = int(input("Enter your bank account number : "))
            self.total = float(input("Enter your Total Balance : "))
            print("\n\t**Your details get saved**")
        except Exception as f:
            print("\nEnter valid details")

    def showData(self):
        print(f"\nName = {self.name}")
        print(f"Account type = {self.type}")
        print(f"Account number = {self.account}")

    def savingInFile(self):
        with open("data.txt", "a") as f:
            f.write(f'''\nName = {self.name}\nAccount type = {self.type}\nAccount number = {self.account}
            Balance = {self.total}\n''')
            

    def ShowBalance(self):
        self.total+= self.amount
        print(f"\n Your Total Account balance = {self.total}")

    def withdrawMoney(self):
        withdraw = float(input("\nEnter amount to withdraw : "))
        self.avail_bal = self.total - withdraw
        print(f"\nYour Available balance = {self.avail_bal}")

    def Deposit(self):
        self.amount = float(input("\nEnter amount to deposit : "))
        print("Your Money get deposited")


machine = ATM_Machine()

while(True):
    print("\n\t\t**Welcome to ATM machine**")

    message = '''\nChoose option :
            1) Enter Details.
            2) Show details.
            3) Balance Enquiry.
            4) Withdraw Money.
            5) Deposit Money.
            6) Exit.'''

    print(message)
    choose = int(input("\nEnter your choice : "))

    if(choose == 1):
        machine.getData()
    
    elif(choose == 2):
        machine.showData()
        machine.savingInFile()

    elif (choose == 3):
        machine.ShowBalance()
    
    elif (choose == 4):
        machine.withdrawMoney()

    elif (choose == 5):
        machine.Deposit()
    
    elif (choose == 6):
        print("\n\t\t**THANKS FOR CHOOSING OUR SERVICES**")
        exit()

    else:
        print("\nInvalid choice")