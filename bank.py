class BankAccount:
# class variable
    min_balance = 1000
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    # create object method for deposit
    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount")
        else:
            self.balance += amount
            print("Deposit successful")

    # object method for withdraw
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
        elif self.balance - amount < BankAccount.min_balance:
            print("Cannot withdraw. Minimum balance must be maintained")
        else:
            self.balance -= amount
            print("Withdrawal successful")

    # object method for display
    def display(self):
        print("Account Number :", self.acc_no)
        print("Account Holder :", self.name)
        print("Balance        :", self.balance)
        print("Minimum Balance:", BankAccount.min_balance)

    # class method – update minimum balance
    @classmethod
    def update_min_balance(cls, new_balance):
        cls.min_balance = new_balance

#Create an object of BankAccount
acc1 = BankAccount(101, "Varsha", 5000)

print("Initial Account Details")
acc1.display()

print("\nDepositing 2000")
acc1.deposit(2000)
acc1.display()

print("\nWithdrawing 3000")
acc1.withdraw(3000)
acc1.display()

print("\nUpdating minimum balance to 2000")
BankAccount.update_min_balance(2000)

print("\nFinal Account Details")
acc1.display()