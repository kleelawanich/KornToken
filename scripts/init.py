from brownie import KornGold, KornToken, accounts

def main():
    kornGold = KornGold.deploy({'from': accounts[0]})
    kornToken = KornToken.deploy("KornToken", "KTN", kornGold.address, {'from': accounts[0]})
