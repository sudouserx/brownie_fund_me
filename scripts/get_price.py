from brownie import FundMe
from scripts.helpful_scripts import get_account
import os

def get_price():
    # get which deployed version i want to interact with 
    fund_me = FundMe[-1] # get the leatest deployed contract
    price = fund_me.getPrice()
    print(price)


def main():
    get_price()