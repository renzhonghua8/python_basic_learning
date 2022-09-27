"""
某公司，账户余额有1w元，给20名员工发工资。
员工编号1到20，从编号1开始，一次领取工资，每人可领取1000元
领工资时，财务判断员工的绩效分（1-10）（随机生成），如果低于5，不发工资，换下一位
如果工资发完了，结束发工资
"""
import random

money = 10000
for x in range(1,21):
    jx = random.randint(1, 10)
    if jx < 5:
        print(f"员工{x},绩效分{jx},低于5,不发工资,下一位")
    else:
        money = money-1000
        print(f"向员工{x},发放工资1000元,账户余额还剩余{money}元")
        if money <= 0:
            break
print("工资发完了，下月领取吧")
