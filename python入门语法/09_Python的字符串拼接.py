# 字符串字面量之间的拼接
print("学IT来黑马"+"月薪过万")
# 字符串字面量和字符串变量的拼接
name = "黑马程序员"
address = "建材城东路9号院"
tel = 17608524562
#typeerror 类型错误
#print("我是："+name+",我的地址是:"+address+",我的电话是:"+tel)
# 把数字修改成字符串拼接
print("我是："+name+",我的地址是:"+address+",我的电话是:%s",tel)
