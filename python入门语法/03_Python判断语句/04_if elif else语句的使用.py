"""
演示 if elif else多条件判断语句的使用
"""

print("欢迎来到黑马动物园")
# 可以在判断条件里面直接输入变量
# height = int(input("请输入你的身高（cm）："))
# vip_level = int(input("请输入你的VIP等级（1-5）："))
# day = int(input("请告诉我今天几号："))
# 通过if判断，可以使用多条件判断的语法
# 第一个条件就是if
# if和elif互斥 满足一个另外一个就不生效
# else也可以省略不写，效果等同独立的if判断
if int(input("请输入你的身高（cm）：")) < 120:
    print("身高小于120cm，可以免费。")
elif int(input("请输入你的VIP等级（1-5）：")) > 3:
    print("VIP级别大于3，可以免费。")
elif int(input("请告诉我今天几号：")) == 1:
    print("今天是1号免费日，可以免费")
else:
    print("不好意思，条件都不满足，需要买票10元。")