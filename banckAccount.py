class Account ():
    def __init__(self, owner, amount, balance):
        self.owner = owner
        self.balance = balance
        self.amount = amount

    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: ${self.balance}"

    def add_deposit(self):
        self.balance = self.balance + self.amount
        print("Deposit Accepted")
        print(f" amount is : {self.amount}")
        print(f" new balance is : {self.balance}")
        return self.balance

    def add_withdraw(self):
        if self.amount > self.balance:
            print("Withdrawal Declined")
        else:
            self.balance = self.balance - self.amount*2
            print("Withdrawal Accepted")
            print(f"Amount withdrawn: {self.amount}")
            print(f"New balance is: {self.balance}")


acc1 = Account(owner="John Doe", balance=-100, amount=50)
acc2 = Account(owner="Gini Doe", balance=0, amount=50)

print(acc1, '\n')
acc1.add_deposit()
acc1.add_withdraw()

print('\n', acc2)
acc2.add_deposit()
acc2.add_withdraw()
