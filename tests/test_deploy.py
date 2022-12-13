from brownie import FundMe, accounts

def test_deploy():
    #arrange 
    account = accounts[0]
    #act
    fund_me = FundMe.deploy({"from": account})
    owner = fund_me.getOwner(); 
    #assert
    assert account == owner

def main():
    test_deploy()