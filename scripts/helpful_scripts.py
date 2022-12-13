from brownie import accounts, network, config , MockV3Aggregator
from web3 import Web3

LOCAL_BLOCKCHAIN_ENVIRONMENT= ["development", "ganache-local"]
DECIMALS = 8
STARTING_PRICE = 200000000000

def get_account():
    if(network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENT):
        return accounts[0] # use the first random account
    else:
        # return accounts.add(os.getenv("PRIVATE_KEY"))
        return accounts.add(config["wallets"]["from_key"])

def deploy_mocks():
    print("Deploying mock ...")
    mock_aggregator= MockV3Aggregator.deploy(DECIMALS, Web3.toWei(STARTING_PRICE, "ether"), {"from":accounts[0]})
    return mock_aggregator

def get_price_address():
    if(network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENT):
        return config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        if len(MockV3Aggregator) > 0: # if there is an already deployed mock Aggregator, --> use the latest one 
            print("using existing mock ...")
            mock_aggregator = MockV3Aggregator[-1]
            # return mock_aggregator.address
        else:
            mock_aggregator = deploy_mocks()
            # return mock_aggregator.address
        return mock_aggregator.address
