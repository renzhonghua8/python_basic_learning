"""
定义两个变量，用以获取从键盘输入的内容，并给出提示信息：
·变量1,变量名：user_name,记录用户名称
·变量2,变量名：user_type,记录用户类型
并通过格式化字符串的形式，通过print语句输出欢迎信息，如下：
您好：黑马程序员，您是尊贵的SSSSSVIP用户，欢迎您的光临
"""
user_name = input("输入姓名")
user_type = input("输入类型")
user_name1 = str(user_name)
user_type1 = str(user_type)
message = "您好：%s,您是尊贵的：%s 用户，欢迎您的光临" % (user_name1,user_type1)
print(message)
