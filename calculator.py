# calculator.py

def calculator():
    print("欢迎使用简单 Python 计算器！")
    print("支持 +, -, *, /, ** (幂运算), % (取余)")
    print("输入 'q' 退出程序\n")
    
    while True:
        try:
            expr = input("请输入算式 (例如: 23 + 45): ").strip()
            if expr.lower() == 'q':
                print("感谢使用，再见！")
                break
                
            # 使用 eval 进行计算 (演示用，实际生产环境建议使用更安全的解析方式)
            if any(op in expr for op in ['+', '-', '*', '/', '**', '%']):
                result = eval(expr)
                print(f"结果 = {result}\n")
            else:
                print("请输入正确的算式！\n")
        except Exception:
            print("输入格式有误，请重试！\n")

if __name__ == "__main__":
    calculator()