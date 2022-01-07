pragma solidity ^0.8.9;

// SPDX-License-Identifier: MIT
import "OpenZeppelin/openzeppelin-contracts@4.2.0/contracts/token/ERC20/ERC20.sol";

contract KornGold is ERC20{

    constructor() ERC20("KornGold", "KGD"){
        _mint(msg.sender, 100 * 10**18);
    }
}
