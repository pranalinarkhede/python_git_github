import uuid

class BankAccount:
    
    def __init__(self, account_type):
        self._account_type = account_type
        self._balance = 0
        self._account_number = uuid.uuid4().hex

    @property
    def balance(self):
        return self._balance
    
    @property
    def account_number(self):
        return self._account_number
    
    @property
    def account_type(self):
        return self._account_type
    