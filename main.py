from fastapi import FastAPI
from bank import BankAccount

app=FastAPI()
account=BankAccount(1000)

@app.get('/')
def home():
    return {'message':'bank API running..'}

@app.get('/balance')
def get_balance():
    return {'balance':account.get_balance()}

@app.post('/deposit/{amount}')
def deposit(amount:int):
    newbalance=account.deposit(amount)
    return {'new_balance':newbalance}
