# 盒子：字符串 input 打他 函数签名
# 机器1：解析 abi 提取选择器 解码参数
# 机器2：打印函数名 打印参数列表

import json
from web3 import Web3

def main():
    # 盒子：接收用户输入
    abi_str = input("请粘贴 ABI（JSON 格式，支持单行或多行）：\n").strip()
    input_data = input("\n请输入交易 input data（十六进制，带或不带 0x 均可）：\n").strip()
    func_sig = input("\n请输入函数签名（如 transfer(address,uint256)），留空则自动从 input 推断：\n").strip()

    # 机器1：解析 ABI、提取选择器、解码参数
    abi = json.loads(abi_str)
    w3 = Web3()

    # 统一补齐 0x
    if not input_data.startswith("0x"):
        input_data = "0x" + input_data

    # 取前 4 字节作为函数选择器
    selector = input_data[:10]  # 0x + 8 hex chars = 4 bytes

    # 在 ABI 里找匹配的函数
    func_abi = None
    for item in abi:
        if item.get("type") == "function":
            # 计算该函数的选择器
            sig = f"{item['name']}({','.join(inp['type'] for inp in item.get('inputs', []))})"
            if w3.keccak(text=sig)[:4].hex() == selector[2:]:
                func_abi = item
                break

    if not func_abi:
        print("❌ 在 ABI 中找不到匹配的函数（选择器:", selector, ")")
        return

    func_name = func_abi["name"]
    input_types = [inp["type"] for inp in func_abi.get("inputs", [])]

    # 解码参数（跳过前 4 字节选择器）
    decoded = w3.codec.decode(input_types, bytes.fromhex(input_data[10:]))

    # 机器2：打印结果
    print(f"\n=== 解码结果 ===")
    print(f"函数名: {func_name}")
    print(f"选择器: {selector}")
    print(f"参数列表:")
    inputs = func_abi.get("inputs", [])
    names = [inp.get("name", f"param{idx}") for idx, inp in enumerate(inputs)]
    for name, typ, val in zip(names, input_types, decoded):
        # 地址类型格式化
        if typ == "address" and isinstance(val, bytes):
            val = "0x" + val.hex()
        elif typ == "address":
            val = Web3.to_checksum_address(val)
        print(f"  {name} ({typ}): {val}")


if __name__ == "__main__":
    main()