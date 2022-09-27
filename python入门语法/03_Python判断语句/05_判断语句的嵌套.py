"""
演示判断语句的嵌套使用
"""
# if int(input("你的身高是多少：（cm）")) > 120 :
#     print("身高超出限制，不可以免费")
#     print("但是，如果vip级别大于3，可以免费")
#     if int(input("请输入你的vip级别")) > 3:
#         print("恭喜你，vip级别达标，可以免费")
#     else:
#         print("身高和vip级别都不达标，请补票10元。")
# else:
#     print("恭喜你，你可以免费游玩")

# """
# 1.必须是大于等于18岁小于30岁的成年人
# 2.同时入职时间需大于两年，或者级别大于3才可以领取
# """
age = int(input("请输入年龄"))

if age >= 18:
   print("你已经成年")
   if age <30:
       print("年龄达标了")
       time = int(input("请输入入职时间:"))
       level = int(input("请输入级别："))
       if time>2:
           print("恭喜，年龄和入职时间都满足你可以领取")
       elif level>3:
           print("恭喜，年龄和级别满足你可以领取")
       else:
           print("您不满足条件2，不能领取")
   else:
       print("年龄太大了，不好意思")
else:
    print("未成年，不可以领取")