"""
Bank Account module

"""
class BankAccount:
    """Simple Bank Account"""
    def __init__(self,balance=0):
        self.balance=balance

    def deposit(self,amount):
        """Deposit"""
        if amount<0:
            raise ValueError("deposit amount must be positive")
        self.balance+=amount
        return self.balance

    def withdraw(self,amount):
        """withdrawal"""
        if amount>self.balance:
            raise ValueError("insufficient balance")
        if amount<=0:
            raise ValueError("withdraw amount must be positive")
        self.balance-=amount
        return self.balance

    def get_balance(self):
        """checking balance"""
        return self.balance
