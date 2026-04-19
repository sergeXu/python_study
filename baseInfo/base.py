# 基础环境检查 macOS
# python3 --version

print("Hello World")
print("\n*** 变量基础 ***")
msg = "Hello World"
print(msg)
print(type(msg))

# 大小写
name = "serge xu"
print(name.upper())
print(name.lower())
print(name.title())

firstName = "serge"
lastName = "xu"
# f字符串
fullname = f"{firstName}__{lastName}"
print(fullname.title())
# 缩进添加空白
print("Languages:\n\t\tPython\n\tJavaScript\n\tC++")

# 删除空白
str = " python "
print(str.rstrip())
print(str.lstrip())
print(str.strip())

print("\n*** 数部分 ***")
# 乘方运算
m = 3 ** 2
print(m)
w = (2+3) * 4 -1
print(w)

# “无论是哪种运算，只要有操作数是浮点数，Python默认得到的总是浮点数，即便结果原本为整数也是如此”
print("整除结果也是浮点数")
q = 4/2
print(q, type(q))
print( f"浮点数运算:{1+2.0}")

#同时赋值多个变量
x,y,z = 1,2,3
print(x,y,z)

# 常量 （非强制控制不能修改）
MAX_VALUE = 100
print(MAX_VALUE)


