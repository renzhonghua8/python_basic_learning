"""
定义一个函数，名称任意，并接收一个参数传入（数字类型，表示体温）
在函数内进行体温判断（正常范围：小于等于37.5），并输入如下内容
"""

def check(temperature):
    if temperature <=37.5:
        print(f"体温测量中,您的体温是：{temperature}度，体温正常请进！")
    else:
        print(f"体温测量中,您的体温是：{temperature}度，需要隔离！")
if __name__ == '__main__':
    print("欢迎来到黑马程序员！请出示您的健康码以及72小时核酸证明，并配合测量体温！")
    temperature = float(input(f"请输入你的体温\n"))
    check(temperature)