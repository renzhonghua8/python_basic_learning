mylist = [21,25,21,23,22,20]
mylist.append(31)
print(mylist)
mylist.extend([29,33,30])
print(mylist)

num1 = mylist[1]

print(num1)
num2 = mylist[-1]

print(num2)
index = mylist.index(31)
print(index)
print(f"{mylist}")