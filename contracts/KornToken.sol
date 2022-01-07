pragma solidity ^0.8.9;

// SPDX-License-Identifier: MIT
import "OpenZeppelin/openzeppelin-contracts@4.2.0/contracts/token/ERC20/IERC20.sol";
import "OpenZeppelin/openzeppelin-contracts@4.2.0/contracts/token/ERC20/ERC20.sol";
/**
    @title Bare-bones Token implementation
    @notice Based on the ERC-20 token standard as defined at
            https://eips.ethereum.org/EIPS/eip-20
 */
contract KornToken is ERC20{

    uint256 public exchangeRate;
    IERC20 public kornGold;

    mapping(address => uint256) balances;
    mapping(address => mapping(address => uint256)) allowed;

    constructor(
        string memory _name,
        string memory _symbol,
        address _kornGoldAddress
    )
    ERC20(_name, _symbol)
    {
        exchangeRate = 10; // 10 kornGold = 1 KornToken
        kornGold = IERC20(_kornGoldAddress);
    }

    /**
        @notice Transfer kornGold to this contract for minting KornToken
        @param _value The amount of kornGold to be transferred
        @return Success boolean
     */
    function mint(uint256 _value) public returns (bool) {
        require (kornGold.allowance(msg.sender, address(this)) >= _value, "Insufficient allowance");
        kornGold.transferFrom(msg.sender, address(this), _value);
        uint _amount = _value / exchangeRate;
        _mint(msg.sender, _amount);
        return true;
    }

    /**
        @notice Burn KornToken to get back kornGold
        @param _value The amount of KornToken to be burned
        @return Success boolean
     */
    function burn(uint256 _value) public returns (bool) {
        require(balances[msg.sender] >= _value, "Insufficient balance");
        _burn(msg.sender, _value);
        kornGold.transfer(msg.sender, _value * exchangeRate);
        return true;
    }
}
