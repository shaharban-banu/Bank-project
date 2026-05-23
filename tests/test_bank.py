import pytest
from bank import BankAccount

def test_initial_balance():
    account=BankAccount()
    assert account.get_balance()==0

def test_deposit(account):
    newbalance=account.deposit(500)
    assert newbalance==1500

def test_withdraw(account):
    newbalance=account.withdraw(300)
    assert newbalance==700

def test_withdraw_insufficient_balance(account):
    with pytest.raises(ValueError):
        account.withdraw(3000)

def test_invalid_deposit(account):

    with pytest.raises(ValueError):
        account.deposit(-100)
