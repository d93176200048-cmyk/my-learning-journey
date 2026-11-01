// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// 这是一个能存一个数字、也能把数字取出来的合约
contract StoreNumber {
    // 状态变量：存在链上的数字（合约的"记忆"）
    uint256 myNumber;

    // store：把传进来的数字存起来（改状态，要烧油）
    function store(uint256 newNumber) public {
        myNumber = newNumber;
    }

    // retrieve：把存着的数字取出来（只读，不改状态，不烧油）
    function retrieve() public view returns (uint256) {
        return myNumber;
    }
}