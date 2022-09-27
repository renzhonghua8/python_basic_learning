"""
案例需求：定义一个数字（1-10，随机产生），通过3次判断来猜出数字
案例要求：
1.数字随机产生，范围1-10
2.有3次机会猜测数字，通过3层嵌套判断实现
3.每次猜不中，会提示大了或小了
"""
import random
num = random.randint(1,10)
key = int(input("请输入第一次猜测的数字"))
if key == num:
    print("第一次就猜对了，你太牛了")
else:
    if(key>num):
        print("你猜测的数字大了")
    else:
        print("你猜测的数字小了")
    key = int(input("请输入第二次猜测的数字"))
    if key == num:
        print("恭喜你，第二次猜对了")
    else:
        if(key>num):
            print("你猜测的数字大了")
        else:
            print("你猜测的数字小了")
            key = int(input("请输入第三次猜测的数字"))
        if key == num:
            print("恭喜你，第三次猜对了")
        else:
            print("Sorry,三次都猜错了")