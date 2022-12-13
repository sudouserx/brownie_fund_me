from brownie import FundMe, accounts

def test_get_price():
    #arrangement
    account = accounts[0]
    fund_me = FundMe.deploy({"from":account})
    # step 2--> the computation 
    price = fund_me.getPrice()
    # step 3 --> checking the result 
    # assert price != 
    pass

def main():
    test_get_price()