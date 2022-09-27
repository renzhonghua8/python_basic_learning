"""
定义一个全局变量：money，用来记录银行卡余额（默认5000000）
定义一个全局变量：name，用来记录客户姓名（启动程序时输入）
定义如下的函数：
·查询余额函数
·存款函数
·取款函数
·主菜单函数
要求：
程序启动后要求输入客户姓名
查询余额、存款后，取款后都会返回主菜单
存款、取款后，都应显示一下当前余额
客户选择退出或输入错误，程序会退出，否则一直运行
"""

def yue():
    global money
    # money = money-cunkuan()
    print(f"{name},您好，您的余额为{money}元")
    zhucaidan()
def cunkuan():
    print(f"-----存款-----")
    cunkuan_yuan = int(input(f"请输入您的存款金额"))
    print(f"{name},您好，你存款{cunkuan_yuan}元成功")
    global money
    money = money + cunkuan_yuan
    print(f"{name},您好，你的余额剩余：{money}元")
    zhucaidan()
def qukuan():
    print(f"-----取款-----")
    qukuan_yuan = int(input(f"请输入您的取款金额"))
    print(f"{name},您好，你存款{qukuan_yuan}元成功")
    global money
    money = money - qukuan_yuan
    print(f"{name},您好，你的余额剩余：{money}元")
    zhucaidan()
def zhucaidan():
    print("-----主菜单-----")
    global money
    money = 50000000

    print(f"{name},您好，欢迎来到黑马银行ATM。请选择操作:")
    print("f查询余额\t[输入1]")
    print("f存款\t[输入2]")
    print("f取款\t[输入3]")
    print("f退出\t[输入4]")
    key = int(input(f"请输入操作指令"))
    if key == 1:
        yue()
    if key == 2:
        cunkuan()
    if key ==3:
        qukuan()
    else:
        exit()


if __name__ == '__main__':
    global name
    name = str(input(f"请输入你的姓名"))
    zhucaidan()
