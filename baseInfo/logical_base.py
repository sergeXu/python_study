# if语句
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
          print(car.upper())
    else:
          print(car.title())

# 条件组合 and or
print("\n 条件组合")
age0,age1 = 16,21
check = age0> 15 and age1 < 20
print(check)

requested_toppings = ['mushrooms', 'onions', 'pineapple']
print("onions" in requested_toppings)
print("onions" not in requested_toppings)

# if elif else结构
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")

# 输出序数
number = list(range(1,10))
for i in number:
    if i == 1 :
        print(f"{i}st")
    elif i == 2 :
        print(f"{i}nd")
    elif i == 3 :
        print(f"{i}rd")
    else:
        print(f"{i}th")


