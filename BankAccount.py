class BankAccount:
   
    def __init__(self, account_name, starting_balance):
        self.account_name = account_name
        self.balance = starting_balance
    
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Not enough money in account to withdrawl")

    def get_balance(self):
        return f"{self.account_name} has a balance of ${self.balance}"