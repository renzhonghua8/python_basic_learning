"""
演示数据容器之：list列表
语法：[元素，元素，...]
"""

# 定义一个列表list
my_list = ["itheima","itcast","python"]
print(my_list)
print(type(my_list))
# 定义一个和嵌套的列表
my_list = [[1,2,3],[4,5,6]]
print(my_list)
print(type(my_list))
# 通过下标索引去除对应位置的数据
my_list =["Tom","Lily","Rose"]
# 列表[下标索引]，从前到后0，1，2  从后往前-1，-2，-3
print(my_list[0])
print(my_list[-3])
print(my_list[1])
print(my_list[-2])
print(my_list[2])
print(my_list[-1])
# 错误示范，通过下标索引取数据，一定不要超过范围
# print(my_list[3])

# 取出嵌套列表的元素
my_list = [[1,2,3],[4,5,6]]
print(my_list[1][1])