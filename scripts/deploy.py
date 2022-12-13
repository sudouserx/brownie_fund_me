from brownie import FundMe, network, config, accounts
from scripts.helpful_scripts import get_account, get_price_address


def deploy_fund_me():
    account = get_account()
    price_address = get_price_address()
    fund_me = FundMe.deploy(price_address,{"from":account}, publish_source=config["networks"][network.show_active()].get("verify"))
    # print(fund_me)

    return fund_me

def main():
    deploy_fund_me()