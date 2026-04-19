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

