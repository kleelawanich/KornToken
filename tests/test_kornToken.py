import brownie

def test_owner_balance(kornGold, accounts):
    assert kornGold.totalSupply() > 0
    assert kornGold.balanceOf(accounts[0]) == kornGold.totalSupply()


def test_initial_total_supply_is_zero(kornToken):
    assert kornToken.totalSupply() == 0

def test_mint_new_token(kornToken, kornGold, accounts):
    userGoldBalance = kornGold.balanceOf(accounts[0])
    kornGoldAmount = userGoldBalance / 2
    kornGold.approve(kornToken.address, userGoldBalance, {'from': accounts[0]})
    tx = kornToken.mint(kornGoldAmount, {'from': accounts[0]})
    mintedAmount = kornGoldAmount / kornToken.exchangeRate()

    assert tx.return_value is True
    assert kornToken.balanceOf(accounts[0]) == mintedAmount
    assert kornToken.totalSupply() == mintedAmount
    assert kornGold.balanceOf(accounts[0]) == userGoldBalance - kornGoldAmount
    assert kornGold.balanceOf(kornToken.address) == kornGoldAmount
    

def test_mint_new_token_zero_amount(kornToken, kornGold, accounts):
    tokenSupply = kornToken.totalSupply()
    userTokenBalance = kornToken.balanceOf(accounts[0])
    userGoldBalance = kornGold.balanceOf(accounts[0])
    contractGoldBalance = kornGold.balanceOf(kornToken.address)
    tx = kornToken.mint(0, {'from': accounts[0]})
    
    assert tx.return_value is True
    assert kornToken.balanceOf(accounts[0]) == userTokenBalance
    assert kornToken.totalSupply() == tokenSupply
    assert kornGold.balanceOf(accounts[0]) == userGoldBalance
    assert kornGold.balanceOf(kornToken.address) == contractGoldBalance
    

def test_insufficient_mint_new_token(kornToken, accounts):
    with brownie.reverts():
        kornToken.mint(1, {'from': accounts[0]})

def test_burn_token(kornToken, kornGold, accounts):
    tokenSupply = kornToken.totalSupply()
    tokenBalance = kornToken.balanceOf(accounts[0])
    tokenAmount = tokenBalance / 2
    userGoldBalance = kornGold.balanceOf(accounts[0])
    contractGoldBalance = kornGold.balanceOf(kornToken.address)
    tx = kornToken.burn(tokenBalance, {'from': accounts[0]})
    returnGold = tokenAmount * kornToken.exchangeRate()

    assert tx.return_value is True
    assert kornToken.balanceOf(accounts[0]) == tokenBalance - tokenAmount
    assert kornToken.totalSupply() == tokenSupply - tokenBalance
    assert kornGold.balanceOf(accounts[0]) == userGoldBalance + returnGold
    assert kornGold.balanceOf(kornToken.address) == contractGoldBalance - returnGold

def test_burn_zero_token(kornToken, kornGold, accounts):
    tokenSupply = kornToken.totalSupply()
    userTokenBalance = kornToken.balanceOf(accounts[0])
    userGoldBalance = kornGold.balanceOf(accounts[0])
    contractGoldBalance = kornGold.balanceOf(kornToken.address)
    tx = kornToken.burn(0, {'from': accounts[0]})
    
    assert tx.return_value is True
    assert kornToken.balanceOf(accounts[0]) == userTokenBalance
    assert kornToken.totalSupply() == tokenSupply
    assert kornGold.balanceOf(accounts[0]) == userGoldBalance
    assert kornGold.balanceOf(kornToken.address) == contractGoldBalance

def test_insufficient_burn_token(kornToken, accounts):
    with brownie.reverts():
        kornToken.burn(1, {'from': accounts[0]})

