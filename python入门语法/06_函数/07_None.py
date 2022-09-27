"""
演示特殊字面量None
"""
# 无return语句的函数返回值
def say_hi():
     print("hello")
result = say_hi()
print(f"无返回值函数，返回的内容是：{result}")
print(f"无返回值函数，返回的内容是：{type(result)}")

# 主动返回None
def say_hi1():
    print("hello")
    return None


result = say_hi1()
print(f"you返回值函数，返回的内容是：{result}")
print(f"you返回值函数，返回的内容是：{type(result)}")
# None用于if判断
def check_age(age):
    if age > 18:
        return "success"
    else:
        return None
result = check_age(16)
if not result:
    print("未成年，不可以进入")
# None用于声明无初始内容的变量
name =None