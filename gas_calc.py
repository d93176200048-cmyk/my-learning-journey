# 盒子：用户的gas费花费 gas费单价 eth价格 换算成人民币的汇率
# 机器1：算 wei 算 eth 算 cny
# 机器2：打印结果

def main():
    # 盒子：接收用户输入的四个数字
    gas_used = int(input("请输入 gasUsed（例如 21000）："))
    gas_price = int(input("请输入 gasPrice（单位 wei，例如 20000000000 即 20 gwei）："))
    eth_price_usd = float(input("请输入 ETH 当前价格（USD，例如 2400）："))
    usd_to_cny = float(input("请输入 USD→CNY 汇率（例如 7.2）："))

    # 机器1：逐步换算
    wei = gas_used * gas_price                    # 总 wei
    eth = wei / 1e18                              # wei → ETH
    usd = eth * eth_price_usd                     # ETH → USD
    cny = usd * usd_to_cny                        # USD → CNY

    # 机器2：打印结果
    print(f"\n=== Gas 费换算结果 ===")
    print(f"gasUsed:     {gas_used}")
    print(f"gasPrice:    {gas_price} wei ({gas_price / 1e9:.1f} gwei)")
    print(f"总计:        {wei} wei")
    print(f"折合 ETH:    {eth:.8f} ETH")
    print(f"折合 USD:    ${usd:.4f}")
    print(f"折合 CNY:    ¥{cny:.4f}")


if __name__ == "__main__":
    main()