from scripts.helpful_scripts import get_account, get_price_address
from scripts.deploy import deploy_fund_me

def test_can_fund_and_withdraw():
    # arrange
    account = get_account()
    fund_me = deploy_fund_me()

    #act
    fund_amount = 2
    print("Funding ...")
    tx = fund_me.fund({"from":account, "value": fund_amount})
    tx.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == fund_amount
   
    print("Withdrawing ...")
    tx2 = fund_me.withdraw({"from": account})
    tx2.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == 0
