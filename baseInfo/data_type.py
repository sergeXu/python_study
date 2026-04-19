# 列表
bicycles = ["trek","cannondale","redline","specialized"]
print(bicycles,type(bicycles))
print(bicycles[0],type(bicycles[0]))
# 最后n个元素
print(bicycles[-1])
print(bicycles[-2])

# 修改列表
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# 添加元素 - 队列尾
motorcycles.append('ducati2')
print(motorcycles)
# 任意位置添加
motorcycles.insert(1,"ninebot")
print(motorcycles)

motorcycles2 = motorcycles.copy()
# 删除元素
del motorcycles[0]
print(motorcycles)
# pop默认队列尾，栈结构
temp = motorcycles.pop()
print(temp)
print(motorcycles)

temp = motorcycles2.pop(0)
print(temp)
print(motorcycles2)

# 根据值删除 yamaha, 注意只删除了第一个匹配的值
motorcycles2.remove("yamaha")
print(motorcycles2)

print("\n*** 排序 ***")
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars2 = cars.copy()
# 默认字典排序并保存 sort()
cars.sort()
print("排序",cars)
cars.sort(reverse=True)
print("逆序",cars)
# 排序不保存 sorted()
print("排序不保存",sorted(cars2))
print("排序不保存",sorted(cars2,reverse=True))
#列表翻转
print(cars2)
cars2.reverse()
print(cars2)
print("列表长度",len(cars))

print("\n*** 操作列表 ***")
