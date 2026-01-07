"""
Exercise 6: Bank Account with Encapsulation

Create a `BankAccount` class with:
- Private attributes: __account_number, __balance, __owner
- Public methods:
  - deposit(amount) - add money (validate > 0)
  - withdraw(amount) - remove money (check sufficient funds)
  - get_balance() - return balance
  - transfer(amount, target_account) - transfer to another account
- Properties:
  - owner - read-only property
  - account_number - read-only property
"""

# TODO: Write your BankAccount class here

class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.__account_number = account_number
        self.__owner = owner
        self.__balance = balance
    @property
    def owner(self):
        return self.__owner
    @property
    def account_number(self):
        return self.__account_number
    ### Public Methods
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError("Deposit amount must be positive")
    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        elif amount <= 0:
            raise ValueError("Withdraw amount must be positive")
        else:
            self.__balance -= amount
    def get_balance(self):
        return self.__balance
    def transfer(self, amount, target_account):
        if amount > self.__balance:
            raise ValueError("Insufficient funds for transfer")
        elif amount <= 0:
            raise ValueError("Transfer amount must be positive")
        else:
            self.withdraw(amount)
            target_account.deposit(amount)    


# Test code (uncomment when ready)
acc1 = BankAccount("ACC001", "Alice", 1000)
acc2 = BankAccount("ACC002", "Bob", 500)
print(f"{acc1.owner}: ${acc1.get_balance()}")
print(f"{acc2.owner}: ${acc2.get_balance()}")
acc1.deposit(200)
acc1.withdraw(150)
acc1.transfer(300, acc2)
print(f"{acc1.owner}: ${acc1.get_balance()}")
print(f"{acc2.owner}: ${acc2.get_balance()}")
