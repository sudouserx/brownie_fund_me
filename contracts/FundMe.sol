// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

// import "../interfaces/AggregatorV3Interface.sol";
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract FundMe {

    // using keywork can be used to check integer overflow , 
    // using SafeMathChainlink for uint256; <-- syntax
    mapping (address => uint256 ) public addressToAmountFunded ; // a mapping of address of the funder and the amount funded 

    address[] public funders; // an array of the funders address , filtered from the mapping above
    AggregatorV3Interface public priceFeed;

    address owner;
    constructor (address _priceFeed) public {
        priceFeed= AggregatorV3Interface(_priceFeed);
        owner = msg.sender;
    }

    function getOwner() public view returns(address) {
        return owner;
    }
    function fund() public payable {

        uint256 minimumAmountToFund = 50 * 10 ** 18 ; 

        require ( getConversionRate(msg.value) >= minimumAmountToFund, "Not enough amount !, more ETH"); // check the funding amount to the minimum amount to fund 

        addressToAmountFunded[msg.sender] += msg.value; // a payable function to fund a given amount
        funders.push(msg.sender);
    }

    function getPrice () public view returns(uint256) {
        (,int256 answer,,,) = priceFeed.latestRoundData();
        return uint256(answer * 10000000000);
    }

    function getConversionRate (uint256 ethAmount ) public view returns(uint256) {
        return uint256(ethAmount * getPrice() / 1000000000000000000); // ethAmountInUSD
    }

    function getEnteranceFee() public view returns(uint256) {
        uint256 minimumUSD = 50*10**10;
        uint256 price = getPrice();
        uint256 precision = 1*10**0;
        return (minimumUSD *precision) / price;
    }

    // modifer : acts as a middleware for a function 
    modifier onlyOwner {
        require (msg.sender == owner); 
        _; // continue executing code 
    }

    function withdraw() payable onlyOwner public {

        payable(msg.sender).transfer(address(this).balance); // transfer all the balance in this contract to the caller of this function 

        for(uint256 i= 0; i<funders.length; i++){ // loop through the funders array, grab the funders address , empty the value stored in the mapping ( address => balance ) for the address
            address funder = funders[i];
            addressToAmountFunded[funder] = 0;
        }

        funders = new address[] (0); // resetting the funder address

    }
}