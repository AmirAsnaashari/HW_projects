from csvHandler import CSVHandler
from datetime import datetime, timedelta

obj = CSVHandler()
try:
    rows, fields = obj.read()

except:
    obj.write(["user_from", "user_to", "type", "amount", "dateTime"])


class BankAccount:
    def __init__(self, minimum_balance, name, balance):
        self.minimum_balance = minimum_balance
        self.name = name
        self.balance = float(balance)
        self.obj_csv = CSVHandler()

    def deposit(self):
        amount = float(input("Enter amount to be deposited: "))
        self.balance += amount
        print("\n Amount deposit:", amount, "\n Your Balance is:", self.balance)
        self.obj_csv.write(rows=[self.name, "", "deposit", amount, datetime.today().now()])

    def withdraw(self):
        amount = float(input("Enter amount to be withdrawn: "))
        if self.__withdraw_permission(amount):
            self.balance -= amount
            print("\n You Withdrew:", amount, "\n Your Balance is:", self.balance)
            self.obj_csv.write(rows=[self.name, "", "withdraw", amount, datetime.today().now()])
        else:
            raise

    def __withdraw_permission(self, amount):
        if amount < self.balance:
            return True
        else:
            return False

    def transfer(self, name):
        print("name : ", name)
        amount = float(input("Enter amount to be transfer: "))
        if self.__withdraw_permission(amount):
            self.balance = self.balance - amount
            self.obj_csv.write(rows=[self.name, name, "transfer", amount, datetime.today().now()])
            print(f'You transferred {amount} to  {name}\nyour balance is {self.balance} now')
        else:
            raise

    def read_transactions_of_account(self):
        rows, fields = self.obj_csv.read()
        print('Field names are:' + ', '.join(field for field in fields))
        print('\nFirst 5 rows are:\n')
        min2plus = datetime.today().now() + timedelta(minutes=2)
        min2mines = datetime.today().now() - timedelta(minutes=2)
        for row in rows:
            record_time = datetime.strptime(row[4], '%Y-%m-%d %H:%M:%S.%f')
            if row[0] == self.name and record_time <= min2plus and  record_time >= min2mines:
                print("\t\t", row)


account_0 = BankAccount(100, 'Amir', 5000)
account_1 = BankAccount(100, 'Ali', 2000)

account_0.deposit()
account_0.withdraw()
print(account_0.transfer(account_1.name))
account_0.read_transactions_of_account()
