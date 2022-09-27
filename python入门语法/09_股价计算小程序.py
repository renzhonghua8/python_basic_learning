"""
定义如下变量：
·name 公司名
·stock_price 当前股价
·stock_code 股票代码
·stock_price_daily_growth_factor 股票每日增长系数，浮点数类型，比如1.2
·growth_days 增长天数
计算，经过growth_days天的增长后，股价达到了多少钱
使用字符串格式化进行输出，如果是浮点数，要求小数点精度2位数
"""
name = "传智播客"
stock_price = 19.99
stock_code = "006032"
stock_price_daily_growth_factor = 1.2
growth_days = 7
end_price = stock_price * stock_price_daily_growth_factor ** growth_days

message1 = f"公司{name},股票代码：{stock_code},当前股价：{stock_price}"
# message2 = f"每日增长系数是:{stock_price_daily_growth_factor},经过{growth_days}天的增长后,股价达到了：{ end_price}"
message3 = "每日增长系数是：%.1f,经过%d天的增长后,股价达到了：%.2f" % (stock_price_daily_growth_factor,growth_days,stock_price*stock_price_daily_growth_factor**growth_days)
print(message1)
# print(message2)
print(message3)
