"""
演示在函数使用的时候，定义的变量作用域
"""
# 演示局部变量
# def test_a():
#     num = 100
#     print(num)
# test_a()
# print(num)
# 演示全部变量
num = 100 #全局变量
def test_a():
    print(f"test_a的num{num}")
def test_b():
    num = 500 # 局部变量
    print(f"test_b的num{num}")
test_a()
test_b()
print(num)
# global关键字，在函数内声明变量为全局变量
num = 100 #全局变量
def test_a():
    print(f"test_a的num{num}")
def test_b():
    global num  # 设置内部定义的变量为全局变量
    num = 500 # 局部变量
    print(f"test_b的num{num}")
test_a()
test_b()
print(num)