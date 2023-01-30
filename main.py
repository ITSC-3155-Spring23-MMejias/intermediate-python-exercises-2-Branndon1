from BankAccount import BankAccount

account = BankAccount("Wally", 100)
account.deposit(23.84)
account.withdraw(53.68)

print(account.get_balance())