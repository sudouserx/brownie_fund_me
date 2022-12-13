from brownie import FundMe 
from scripts.helpful_scripts import get_account, get_price_address


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    enterance_fee = fund_me.getEnteranceFee()
    print(f"enterance fee : {enterance_fee}")
    print("Funding ...")
    fund_me.fund({"from": account, "value": 2})

def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    print("Withdrawing ...")
    fund_me.withdraw({"from": account})

def main():
    fund()
    withdraw()
