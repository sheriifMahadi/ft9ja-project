from bson import ObjectId
import pymongo
import random 
import time
import datetime
import os

mongo_setup = os.environ.get('mongo_setup')
client = pymongo.MongoClient(mongo_setup)
dbname = client['timerapp']
trades = dbname['trades']
accounts = dbname['accounts']


def generate_profit():
    profit = []
    for i in range(10):
        profit.append(round(random.uniform(2.4, 90.6), 2))
    return profit

def generate_loss():
    loss = []
    for i in range(10):
        loss.append(round(random.uniform(0.3, 100), 2))
    return loss

def populate_trades():
    user_trades = [
        {"profit": generate_profit(), "loss": generate_loss()},
        {"profit": generate_profit(), "loss": generate_loss()},
        {"profit": generate_profit(), "loss": generate_loss()},
        {"profit": generate_profit(), "loss": generate_loss()},
        {"profit": generate_profit(), "loss": generate_loss()},
        {"profit": generate_profit(), "loss": generate_loss()},
        {"profit": generate_profit(), "loss": generate_loss()},
        {"profit": generate_profit(), "loss": generate_loss()},
        {"profit": generate_profit(), "loss": generate_loss()},
        {"profit": generate_profit(), "loss": generate_loss()}
    ]
    if trades.count_documents({})< 10:
        all_trades = trades.insert_many(user_trades)
        return "trades creation success"
    return None
    

def populate_account():
    trade_accounts = [
        {"firstname":"Sharon","lastname":"Ferney","email":"sferney0@fastcompany.com", "initial": 100},
        {"firstname":"Gwenneth","lastname":"Garley","email":"ggarley1@ucla.edu", "initial": 100},
        {"firstname":"Dotty","lastname":"Garie","email":"dgarie2@php.net", "initial": 100},
        {"firstname":"Ailis","lastname":"Kilcullen","email":"akilcullen3@fema.gov","initial": 100},
        {"firstname":"Ronny","lastname":"Maxwell","email":"rmaxwell4@t.co", "initial": 100},
        {"firstname":"Cole","lastname":"Rigmond","email":"crigmond5@sitemeter.com","initial": 100},
        {"firstname":"Mal","lastname":"Berthelet","email":"mberthelet6@aboutads.info","initial": 100},
        {"firstname":"Sax","lastname":"McIlheran","email":"smcilheran7@google.de","initial": 100},
        {"firstname":"Ermentrude","lastname":"Dyers","email":"edyers8@wired.com","initial": 100},
        {"firstname":"Agnes","lastname":"Stiger","email":"astiger9@theatlantic.com","initial": 100},
    ]
    if accounts.count_documents({}) < 10:
        allaccounts = accounts.insert_many(trade_accounts)
        return "account creation success"
    return None

# trades 
# accounts

def update_fields():
    if accounts.count_documents({}) < 10 and trades.count_documents({}) < 10:
        for account, trade in zip(accounts.find(), trades.find()):
            # account['trades'] = trade['_id']
            # trade['account'] = account['_id']
            accounts.update_one({"_id": account['_id']}, {"$set": {"trades": trade['_id']}})
            trades.update_one({"_id": trade['_id']}, {"$set": {"account": account['_id']}})

            print(f"account: {account}, trade: {trade}")


def fetch_all_traders():
    traders = accounts.find()
    return traders

def get_trader(id):
    account = accounts.find_one({'_id': ObjectId(id)})
    if account != None:
        trade = trades.find_one({"_id": account['trades']})

    return [account, trade]

def get_trader_by_email(email):
    account = accounts.find_one({'email': email})
    if account != None:
        return [account]
    else: return None

def main():
    populate_account()
    populate_trades()
    update_fields()
    return ""

main()

def generate_time():
    timestamps = []

    for i in range(10):
        curr = f"{datetime.datetime.now().strftime('%I')}:{datetime.datetime.now().minute + i}"
        timestamps.append(curr)
    return timestamps
