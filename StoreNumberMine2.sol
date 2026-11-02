// SPDX-License-Identifier:MIT
pragma solidity ^0.8.0;
contract StoreNumberMine2{
    //状态变量:存一个数字
    uint256 myNumber;
    address owner;
    //函数 1: store,把传进来的数字存起来
    function store(uint256 newNumber)public{
       myNumber=myNumber+newNumber;
    }
    // 函数 2:retrieve,把数字取出来
    function retrieve()public view returns(uint256){
        return myNumber;
    }
    constructor() {
        owner =msg.sender;
    }
    function reset() public {
        require(msg.sender==owner,unicode"主人&#8203;调用者");
        myNumber=0;
    }
} 