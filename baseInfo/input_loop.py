# 基础用法input(),结果默认解析为字符串
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"\nHello, {name}!")

# int()转换为数值
long = '45'
print(long,int(long),type(int(long)))

# while循环
current_number = 1
while current_number < 3:
    print(current_number)
    current_number += 1


# break  continue
print("\n ** break continue")
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
        # break
    print(current_number)

# 删除为特定值的所有列表元素
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)