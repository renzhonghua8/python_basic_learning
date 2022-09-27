"""
1.定义一个变量，数字类型，内容随意。
2.基于input语句输入猜想的数字，通过if和多次elif组合，判断猜想数字是否和心里数字一致。
"""
num = 10
if int(input("请输入第一次猜想的数字：")) == num:
    print("恭喜你第一次就猜对了呢")
elif int(input("不对，再猜一次：")) == num:
    print("猜对了")
elif int(input("不对，再猜最后一次：")) == num:
    print("恭喜，最后一次机会，你猜对了。")
else:
    print("Sorry,全部猜错了，我想的是：10")
