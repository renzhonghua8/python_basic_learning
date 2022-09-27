# 通过占位的形式，完成拼接
name = "黑马程序员"
message = "学IT来:%s" % name
print(message)

# 通过占位的形式，完成数字和字符串的拼接
class_num = 57
avg_salary = 16781
message = "Python大学据学科，北京%s期，毕业平均工资：%s" % (class_num,avg_salary)
print(message)

# 常用占位符 %s,%d,%f 字符串 整数 浮点数
name = "传智播客"
setup_year = 2006
stock_price = 19.99
message = "%s,成立于：%d,我今天的股价是：%f" % (name,setup_year,stock_price)
print(message)
# 快速写法
print(f"我是：{name},成立于：{setup_year},我今天的股价是：{stock_price} ")

num1 = 11
num2 =11.345
print("数字11宽度限制5，结果是：%5d" % num1)
print("数字11宽度限制1，结果是%1d" % num1)
print("数字11.345宽度限制7，小数精度2，结果是：%7.2f" % num2)
print("数字11.345不限制，小数精度2，结果是：%.2f"% num2)


# 字符串格式化，快速写法
# 语法 ： f"内容{变量}" f:format

print(f"我是：{name},成立于：{setup_year},我今天的股价是：{stock_price} ")

# 表达式 ：一条具有明确执行结果的代码语句 如 1+1 、 5*2  or name = “张三” 、 age = 11+11
# 如何格式化表达式
# 1.f"{表达式}"
# 2." %d\%f\%s" % (表达式，表达式，表达式)
print("1+1的结果是：%d" % (1*1))
print(f"1*2的结果是{1*2}")
print("字符串在Python中的类型名是：%s" % type("字符串"))






