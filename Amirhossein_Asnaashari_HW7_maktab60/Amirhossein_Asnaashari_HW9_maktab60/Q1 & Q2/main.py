import main

print(main.deposit())
obj = main.BankAccount(200, 'Ali', 3000)
class BankAccount:
    def __init__(self, minimum_balance, name, balance):
        self.minimum_balance = minimum_balance
        self.name = name
        self.balance = float(balance)

    def deposit(self):
        amount = float(input("Enter amount to be deposited: "))
        self.balance += amount
        print("\n Amount deposit:", amount, "\n Your Balance is:", self.balance)

    def withdraw(self):
        amount = float(input("Enter amount to be withdrawn: "))
        if self.__withdraw_permission(amount):
            self.balance -= amount
            print("\n You Withdrew:", amount, "\n Your Balance is:", self.balance)
        else:
            raise

    def __withdraw_permission(self, amount):
        if amount < self.balance:
            return True
        else:
            return False

    def transfer(self, name):
        amount = float(input("Enter amount to be transfer: "))
        if self.__withdraw_permission(amount):
            self.balance = self.balance - amount
            self.name = name
            return f'You transferred {amount} to {self.name}' \
                   f'\nyour balance is {self.balance} now'
        else:
            raise


test = BankAccount(100, 'Amir', 5000)

print(test.deposit())
print(test.withdraw())
print(test.transfer('Ali'))
