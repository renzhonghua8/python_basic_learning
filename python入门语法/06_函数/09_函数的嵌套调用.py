"""
演示嵌套调用函数
"""
# 定义函数fun_b
def fun_b():
    print("-----b-----")
# 定义函数fun_a, 并在内部调用fun_b
def fun_a():
    print("---------a-----")
    fun_b()
    print("-------c-----")
# 调用函数fun_a
fun_a()