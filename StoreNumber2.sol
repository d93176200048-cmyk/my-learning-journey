// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// StoreNumber2：在 StoreNumber 基础上加"只有部署者能改"
// 接回上次学的：私钥 = 控制权 → Not your keys, not your coins
contract StoreNumber2 {
    // 状态变量
    uint256 myNumber;
    address owner; // 谁部署的这个合约（部署者的"地址"，相当于他的身份证号）

    // 构造函数：合约部署时自动执行一次，把部署者记下来
    constructor() {
        owner = msg.sender; // msg.sender = 当前正在调用这个函数的人
    }

    // store：现在加了门禁 —— 只有 owner 能存
    function store(uint256 newNumber) public {
        require(msg.sender == owner, unicode"你不是主人，无权改数字");
        myNumber = newNumber;
    }

    // retrieve：谁都能读（view，不改状态，不烧油）
    function retrieve() public view returns (uint256) {
        return myNumber;
    }

    // 新增：主人自我介绍
    function whoIsOwner() public view returns (address) {
        return owner;
    }
}