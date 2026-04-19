# 简单 map
alien_0 ={'color':'green','points':5}
print(alien_0['color'],alien_0['points'])
print(alien_0,type(alien_0))
# 添加元素
alien_0['x_position'] = 0
alien_0['y_position'] = 5
print(alien_0)

# 创建新字典
alien_1 ={}
print(alien_1)

# 删除字典中的值
del alien_0['color']
del alien_0['points']
print(alien_0)

# 使用get()访问值
point_value = alien_0.get('points')
print(point_value) # None
# 指定默认值
point_value = alien_0.get('points','No Point')
print(point_value)

print("\n 循环输出")
# “遍历字典时将按插入的顺序返回其中的元素”
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }
for key,value in user_0.items():
    print(key,value)

# 遍历键 可忽略
for key in user_0.keys():
    print(key,user_0[key].title())

# 判断Key值包含
if 'username' in user_0.keys():
    print('username:',user_0['username'])
else :
    print('no username')

# 遍历值
print("\n *** 遍历值 *** ")
if 'efermi' in user_0.values():
    print('efermi')
else :
    print('no efermi')
# 按顺序遍历dict
print("\n *** 按顺序遍历dict *** ")
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# set类型 去重处理
set_data = set(favorite_languages.values())
print("favorite_languages",set_data,type(set_data))

print("\n *** 字典中存储列表 *** ")
# 存储所点比萨的信息。
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }
# 概述所点的比萨。
print(f"You ordered a {pizza['crust']}-crust pizza \n",
      "with the following toppings:")
for topping in pizza['toppings']:
    print("\t"+topping)

