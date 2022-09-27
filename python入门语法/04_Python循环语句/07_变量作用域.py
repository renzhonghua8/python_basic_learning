"""
演示Python for循环临时变量的作用域
"""
# 规范使用

i = 0
for i in range(100):
    print(i)
# 不规范使用
# print(i)
print(i)

