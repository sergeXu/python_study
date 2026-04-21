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

print("\n *** while循环 ***")
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# 标志位 flag
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

# while循环处理列表和字典
print("\n *** while循环处理列表和字典 ***")
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# 验证每个用户，直到没有未验证用户为止。
# 将每个经过验证的用户都移到已验证用户列表中。
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
# 显示所有已验证的用户。
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# 列表删除特定值的元素
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

