"""
通过input语句获取键盘输入的身高
判断身高是否超过120cm，并通过print给出提示信息。
"""
print(f"欢迎来到黑马动物园")
# 定义键盘输入获取身高数据
# input获取到的信息都是字符串，所以需要转换成int类型
height = int(input("请输入你的身高(cm)："))
if height > 120:
    print("您的身高超出120cm,游玩需要购票10元。")
else:
    print("您的身高未超出120cm,可以免费游玩。")
print("祝您游玩愉快。")