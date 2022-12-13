from brownie import FundMe, accounts, network 
import os

def fund():
    account = get_account()
    fund_me = FundMe[-1]

    fund = fund_me.fund({"from": account})

    print(fund)

def get_account():
    if(network.show_active == "development"):
        return accounts[0]
    else:
        return accounts.add(os.getenv("PRIVATE_KEY"))
    

def main():
    fund()