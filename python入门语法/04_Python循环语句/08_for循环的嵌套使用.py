"""
演示嵌套应用for循环
"""
# 坚持表白100天，每天都送10朵花
# range
i= 0
while i<100 :
    i += 1
    print(f"今天是第{i}天表白，坚持...")
    
    for j in range(1,11):
        print(f"给小美送的第{j}次送玫瑰花,坚持...")
    print("小美我喜欢你")
print(f"第{i}天,表白成功")