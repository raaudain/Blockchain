import requests

user = input("Enter user id: ")

def transaction():
    data = requests.get("http://localhost:5000/chain").json()
    
    account_balance = 0
    sent = []
    received = []
    
    print(data)
    
    for block in data["chain"]:
        for action in block["transactions"]:
            if action["sender"] == user:
                account_balance -= action["amount"]
                sent.append(action["amount"], action["recipient"])
                
            if action["recipient"] == user:
                account_balance += action["amount"]
                received.append(action["amount"], action["sender"])
    return account_balance, sent, received

print(transaction())

transaction = transaction()
balance = transaction[0]


print(f"Your current balance is: {balance}")

