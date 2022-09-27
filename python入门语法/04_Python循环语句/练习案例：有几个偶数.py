"""
定义一个数字变量num,内容随意
并使用range()语句,获取从1到num的序列,使用for循环遍历它
在遍历的过程中，统计有多少偶数出现
"""
num = 100
count = 0
for x in range(1,num):
    if x % 2 == 0:
        count += 1
print(f"1到{num}(不含{num}本身)范围内，有{count}个偶数。")

