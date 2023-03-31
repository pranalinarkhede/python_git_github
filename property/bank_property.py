# import uuid

class BankAccount:
    
    def __init__(self):
        # self._account_type = account_type
        self._balance = 0
        # self._account_number = uuid.uuid4().hex

    @property
    def balance(self):
        print("Current balance : ",self._balance)
    
    # @property
    # def account_number(self):
        # return self._account_number
    
    
    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount
    
    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
        
b = BankAccount()
b.deposit(3500)
b.withdraw(400)
print(b.balance)

