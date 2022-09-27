
# print不换行案例
# print("hello",end='')
# print("hello",end='')

# \t相当于tab键，可以让多行字符串进行对齐

# print("hello world")
# print("itheima best")
#
#
# print("hello\tworld")
# print("itheima\tbest")

"""
通过whil循环，输出如下九九乘法表
1.控制行的循环 i <= 9
2.控制每一行输出的循环 j<=i
3.j*i
4.pirnt(j*i,end="")
5.\t
"""

# 定义外层循环的控制变量
i= 1
while i <=9:
    # 定义内层循环的控制变量
    j = 1
    while j<=i:
        # 内层循环的print语句，不要换行，通过\t制表符进行对齐
        print(f"{j} * {i} = {j*i}\t",end='')
        j += 1
    i += 1
    print()# print空内容，就是输出一个换行







