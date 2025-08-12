class Account:
    def __init__(self, bal, acc):
        self.bal = bal
        self.acc = acc

    def debit(self, amount):
        self.bal -= amount
        print("Rs", amount, "was debit")
        print("total balance", self.get_balance())

    def credit(self, amount):
        self.bal += amount
        print("Rs", amount, "was credited")
        print("total balance", self.get_balance())

    def get_balance(self):
        return self.bal


acc1 = Account(10000, 12000)
acc1.debit(5000)
acc1.credit(20000)
