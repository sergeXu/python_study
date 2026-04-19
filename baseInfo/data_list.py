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
magicians =["aa","bb","cc"]
# 注意不要忘记尾部冒号
for magician in magicians:
    print(magician)
    print("run in circle")
print("the circle end")

# 函数range()  打印1~5
for value in range(1,6):
    print(value)
# list() range() 创建数字列表
numbers = list(range(1,11))
print(numbers)
# 指定起始和步长
even_numbers = list(range(2,11,2))
print(even_numbers)

squares =[]
for value in range(1,11):
    squares.append(value**2)
print(squares)

print("\n*** 简单统计计算 ***")
print( min(squares),max(squares),sum(squares))

# 列表解析 [表达式 + for循环]
squares = [value ** 3 for value in range(1,11)]
print(squares)

# 切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
# 索引规则前闭后开，从0开始
print(players[1:3])
print(players[1:])
print(players[:-1])
print("最后3名",players[-3:])
print("前3名",players[:3])

# 找索引
if 'michael' in players:
    print("michael position is",players.index('michael'))

# 复制列表
players2 = players[:]
print("players2",players2)
players2.append("john")
print("players2",players2)
print("players",players)

print("\n*** 元组 tuple - 不可变的列表 ***")
demensions= (200,100)
print(demensions,type(demensions))
print(demensions[0],demensions[1])

# TypeError: 'tuple' object does not support item assignment
# demensions[0] = 300
# print(demensions)

# 不能修改元素，但可以整体赋值
demensions = (400,500)
print(demensions,type(demensions))

