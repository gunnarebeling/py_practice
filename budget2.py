class Category:
    def __init__ (self, name):
        self.name = name
        self.ledger = list()
    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for item in self.ledger:
            items += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + "\n"
            total += item['amount']
        output = title + items + "Total: " + str(total)
        return output
    def deposit (self, amount, description = ""):
        self.ledger.append({"amount": amount, "description": description})
    def withdraw (self, amount, description = ""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True;
        return False
    def get_balance (self):
        balance = 0
        for items in self.ledger:
            balance += items["amount"]
        return balance
    def transfer (self, amount, category):
        if (self.check_funds(amount)):
           self.withdraw(amount + "transfer to" + category.name)
           category.deposit(amount + "transfer from" + self.name)
           return True;
        return False
    def check_funds (self, amount):
        if (self.get_balance() >= amount):
            return True;
        return False
